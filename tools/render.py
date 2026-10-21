#!/usr/bin/env python3
"""Turn a two-host script into a podcast MP3 with Kokoro text-to-speech.

Every paragraph of the script starts with a speaker label, plain or bold.
Headings (lines starting with #) are skipped:

    HOST: Think about how a kid learns what a cat is.

    **COHOST:** Wait, and that works for computers?

Set up the venv with tools/setup.sh, then:

    .venv/bin/python tools/render.py samples/sample.md samples/sample.mp3
    .venv/bin/python tools/render.py script.md out.mp3 --voice COHOST=am_puck
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
import warnings
from contextlib import contextmanager
from pathlib import Path

import numpy as np
import soundfile as sf

REPO_ID = "hexgrad/Kokoro-82M"
RATE = 24000  # Kokoro's sample rate
VOICES = {"HOST": "af_heart", "COHOST": "am_michael"}  # explainer, co-host
TURN_GAP = 0.4  # seconds of silence between paragraphs
SENTENCE_GAP = 0.25  # between the sentence groups a paragraph is split into
GROUP_CHARS = 200  # voices rush on long inputs; ~200 characters is their sweet spot
LUFS = -19  # Apple asks for -16; a mono file plays 3 dB louder on two speakers
PEAK = -2.5  # limiter ceiling in dBFS, leaving room for MP3 overshoot under Apple's -1
LABEL = re.compile(r"\**([A-Z]+):\**\s*(.+)")


def parse(path, voices):
    """Return (speaker, text) for each paragraph of the script."""
    lines = Path(path).read_text().splitlines()
    text = "\n".join(line for line in lines if not line.startswith("#"))
    turns = []
    for para in re.split(r"\n\s*\n", text):
        para = " ".join(para.split())
        if not para:
            continue
        match = LABEL.fullmatch(para)
        if not match:
            sys.exit(f"{path}: paragraph without a speaker label: {para[:60]}")
        if match[1] not in voices:
            sys.exit(f"{path}: unknown speaker {match[1]}, pass --voice {match[1]}=...")
        turns.append((match[1], match[2].replace("*", "")))
    return turns


def sentence_groups(text):
    """Split text at sentence ends into groups of about GROUP_CHARS.

    Very short sentences join their neighbor, since voices are also weak on
    tiny inputs.
    """
    groups = []
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        if groups and (len(groups[-1]) + len(sentence) < GROUP_CHARS or len(sentence) < 40):
            groups[-1] += " " + sentence
        else:
            groups.append(sentence)
    return groups


def silence(seconds):
    return np.zeros(int(seconds * RATE), dtype=np.float32)


def join(clips, gap):
    """Concatenate clips with `gap` seconds of silence between them."""
    out = [clips[0]]
    for clip in clips[1:]:
        out += [silence(gap), clip]
    return np.concatenate(out)


def trim(audio, floor_db=-60):
    """Cut Kokoro's padding, keeping 30 ms before and 80 ms after the speech."""
    loud = np.flatnonzero(np.abs(audio) > 10 ** (floor_db / 20))
    if not loud.size:
        return audio[:0]
    return audio[max(loud[0] - int(0.03 * RATE), 0) : loud[-1] + int(0.08 * RATE)]


def synthesize(turns, voices, speed):
    """Render each turn with its speaker's voice."""
    warnings.filterwarnings("ignore")  # deprecation noise from torch and transformers
    from kokoro import KModel, KPipeline
    from loguru import logger

    logger.remove()  # Kokoro logs every chunk at debug level
    logger.add(sys.stderr, level="WARNING")
    model = KModel(repo_id=REPO_ID).eval()
    pipelines = {}  # one per accent: "a" American, "b" British English
    clips = []
    for n, (speaker, text) in enumerate(turns, 1):
        voice = voices[speaker]
        if voice[0] not in pipelines:
            pipelines[voice[0]] = KPipeline(lang_code=voice[0], repo_id=REPO_ID, model=model)
        pieces = pipelines[voice[0]]("\n".join(sentence_groups(text)), voice=voice, speed=speed)
        clips.append(join([trim(piece.audio.numpy()) for piece in pieces], SENTENCE_GAP))
        print(f"[{n}/{len(turns)}] {speaker}: {text[:60]}", flush=True)
    return clips


def ffmpeg(*args):
    """Run ffmpeg and return its log, which is where it prints measurements."""
    result = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", *args], capture_output=True, text=True)
    if result.returncode:
        sys.exit(result.stderr)
    return result.stderr


@contextmanager
def as_wav(audio):
    with tempfile.NamedTemporaryFile(suffix=".wav") as wav:
        sf.write(wav.name, audio, RATE, subtype="FLOAT")
        yield wav.name


def loudness(audio):
    """Integrated loudness in LUFS, measured by ffmpeg's loudnorm filter."""
    with as_wav(audio) as wav:
        log = ffmpeg("-i", wav, "-af", "loudnorm=print_format=json", "-f", "null", "-")
    return float(json.loads(log[log.rindex("{") :])["input_i"])


def balance(turns, clips):
    """Bring every speaker to the target loudness, so neither host sounds farther away."""
    for speaker in {s for s, _ in turns}:
        mine = [i for i, (s, _) in enumerate(turns) if s == speaker]
        gain = 10 ** ((LUFS - loudness(np.concatenate([clips[i] for i in mine]))) / 20)
        for i in mine:
            clips[i] = clips[i] * gain


def export(audio, path, title):
    """Catch the peaks the loudness gain pushed too high, and encode a mono MP3."""
    limiter = f"alimiter=limit={10 ** (PEAK / 20):.3f}:level=disabled:latency=1"
    with as_wav(audio) as wav:
        ffmpeg("-y", "-i", wav, "-af", limiter, "-ar", "44100", "-ac", "1",
               "-c:a", "libmp3lame", "-b:a", "96k", "-id3v2_version", "3",
               "-metadata", f"title={title}", str(path))


def main():
    parser = argparse.ArgumentParser(description="Render a two-host script to MP3 with Kokoro.")
    parser.add_argument("script", help="Markdown script, one speaker-labeled paragraph per turn")
    parser.add_argument("mp3", help="output file")
    parser.add_argument("--voice", action="append", default=[], metavar="SPEAKER=VOICE",
                        help=f"override a voice (defaults: {VOICES})")
    parser.add_argument("--speed", type=float, default=1.0, help="speaking rate (default 1.0)")
    parser.add_argument("--title", help="MP3 title tag (default: output file name)")
    args = parser.parse_args()

    voices = VOICES | dict(v.split("=", 1) for v in args.voice)
    turns = parse(args.script, voices)
    start = time.time()
    clips = synthesize(turns, voices, args.speed)
    balance(turns, clips)
    audio = np.concatenate([silence(0.3), join(clips, TURN_GAP), silence(0.8)])
    export(audio, args.mp3, args.title or Path(args.mp3).stem)
    print(f"Wrote {args.mp3}: {len(audio) / RATE:.1f} s of audio in {time.time() - start:.0f} s")


if __name__ == "__main__":
    main()
