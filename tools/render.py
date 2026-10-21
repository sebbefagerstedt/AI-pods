#!/usr/bin/env python3
"""Turn a two-host script into a podcast MP3 with VibeVoice.

VibeVoice performs the whole conversation at once, so the hosts react to each
other the way people talking do. Each host's voice is cloned from a short
recording in voices/.

Every paragraph of the script starts with a speaker label, plain or bold.
Headings (lines starting with #) are skipped:

    HOST: Think about how a kid learns what a cat is.

    **COHOST:** Wait, and that works for computers?

Set up the venv with tools/setup.sh, then:

    .venv/bin/python tools/render.py samples/sample.md samples/sample.mp3
    .venv/bin/python tools/render.py script.md out.mp3 --voice COHOST=voices/frank.wav

It runs about 5 times slower than real time on 4 CPUs. Finished segments are
cached in .cache/, so a render that gets interrupted picks up where it stopped.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import warnings
from contextlib import contextmanager
from pathlib import Path

warnings.filterwarnings("ignore")  # deprecation noise from torch and transformers

import numpy as np
import soundfile as sf
import torch
from transformers import AutoModelForTextToWaveform, AutoProcessor, set_seed
from transformers.utils import logging

ROOT = Path(__file__).resolve().parent.parent
MODEL = "vibevoice/VibeVoice-1.5B-hf"
RATE = 24000  # VibeVoice's sample rate
VOICES = {"HOST": ROOT / "voices/alice.wav", "COHOST": ROOT / "voices/carter.wav"}  # explainer, co-host
SEGMENT_CHARS = 3000  # about 3 minutes of speech per generation
LONGEST_PAUSE = 0.7  # seconds; the model sometimes leaves longer gaps between turns
LUFS = -19  # Apple asks for -16; a mono file plays 3 dB louder on two speakers
PEAK = -2.5  # limiter ceiling in dBFS, leaving room for MP3 overshoot under Apple's -1
CACHE = ROOT / ".cache" / "segments"
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


def segments(turns):
    """Group turns into runs of about SEGMENT_CHARS, each generated in one go."""
    groups = [[]]
    for turn in turns:
        if groups[-1] and sum(len(text) for _, text in groups[-1]) + len(turn[1]) > SEGMENT_CHARS:
            groups.append([])
        groups[-1].append(turn)
    return groups


def load_voice(path):
    """Read a recording as 24 kHz mono, the format VibeVoice clones from."""
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(RATE), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(pcm, dtype=np.float32).copy()


def cache_path(segment, voices, seed):
    """Where a segment's audio is cached; changing its text, a voice or the seed misses."""
    used = sorted({speaker for speaker, _ in segment})
    voice_hashes = [hashlib.sha1(Path(voices[speaker]).read_bytes()).hexdigest() for speaker in used]
    key = json.dumps([MODEL, seed, segment, voice_hashes])
    return CACHE / f"{hashlib.sha1(key.encode()).hexdigest()}.wav"


def synthesize(segment, voices, seed, processor, model):
    """Perform one segment of the conversation, cloning each speaker's voice."""
    roles, conversation = {}, []
    for speaker, text in segment:
        content = [{"type": "text", "text": text}]
        if speaker not in roles:  # number speakers by first appearance; give each its voice once
            roles[speaker] = str(len(roles))
            content.append({"type": "audio", "audio": load_voice(voices[speaker])})
        conversation.append({"role": roles[speaker], "content": content})
    inputs = processor.apply_chat_template(
        conversation, return_dict=True, tokenize=True, add_generation_prompt=True
    ).to(model.device, model.dtype)
    set_seed(seed)
    with torch.inference_mode():
        audio = model.generate(**inputs)[0]
    if audio is None:
        sys.exit("VibeVoice generated no audio")
    return audio.float().numpy().squeeze()


def silence(seconds):
    return np.zeros(int(seconds * RATE), dtype=np.float32)


def cap_pauses(audio):
    """Shorten silences longer than LONGEST_PAUSE to that length, cutting out their middle."""
    n = int(0.02 * RATE)  # 20 ms frames
    db = 20 * np.log10(np.abs(audio[: len(audio) // n * n]).reshape(-1, n).max(axis=1) + 1e-9)
    quiet = np.append(db < np.percentile(db, 95) - 35, False)
    half, fade = int(LONGEST_PAUSE / 2 * RATE), int(0.01 * RATE)
    pieces, cut, start = [], 0, None
    for i, q in enumerate(quiet):
        if q and start is None:
            start = i * n
        elif not q and start is not None:
            if i * n - start > 2 * half:
                pieces.append(audio[cut : start + half])
                cut = i * n - half
            start = None
    pieces.append(audio[cut:])
    ramp = np.linspace(1, 0, fade, dtype=np.float32)
    for a, b in zip(pieces, pieces[1:]):  # fade across each cut so it can't click
        a[-fade:] *= ramp
        b[:fade] *= ramp[::-1]
    return np.concatenate(pieces)


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


def export(audio, path, title):
    """Catch the peaks the loudness gain pushed too high, and encode a mono MP3."""
    limiter = f"alimiter=limit={10 ** (PEAK / 20):.3f}:level=disabled:latency=1"
    with as_wav(audio) as wav:
        ffmpeg("-y", "-i", wav, "-af", limiter, "-ar", "44100", "-ac", "1",
               "-c:a", "libmp3lame", "-b:a", "96k", "-id3v2_version", "3",
               "-metadata", f"title={title}", str(path))


def main():
    parser = argparse.ArgumentParser(description="Render a two-host script to MP3 with VibeVoice.")
    parser.add_argument("script", help="Markdown script, one speaker-labeled paragraph per turn")
    parser.add_argument("mp3", help="output file")
    parser.add_argument("--voice", action="append", default=[], metavar="SPEAKER=WAV",
                        help="clone a speaker's voice from this recording "
                             "(defaults: HOST=voices/alice.wav, COHOST=voices/carter.wav)")
    parser.add_argument("--seed", type=int, default=42, help="change it to get a different take")
    parser.add_argument("--title", help="MP3 title tag (default: output file name)")
    args = parser.parse_args()

    voices = VOICES | dict(v.split("=", 1) for v in args.voice)
    groups = segments(parse(args.script, voices))
    start = time.time()
    parts, processor, model = [], None, None
    for n, segment in enumerate(groups, 1):
        path = cache_path(segment, voices, args.seed)
        if not path.exists():
            if model is None:
                logging.set_verbosity_error()
                logging.disable_progress_bar()
                processor = AutoProcessor.from_pretrained(MODEL)
                model = AutoModelForTextToWaveform.from_pretrained(MODEL, dtype=torch.bfloat16).eval()
            CACHE.mkdir(parents=True, exist_ok=True)
            partial = path.with_suffix(".partial.wav")
            sf.write(partial, synthesize(segment, voices, args.seed, processor, model), RATE)
            partial.replace(path)
        parts.append(sf.read(path, dtype="float32")[0])
        print(f"[{n}/{len(groups)}] {len(parts[-1]) / RATE:.0f} s of audio, {time.time() - start:.0f} s so far",
              flush=True)

    audio = cap_pauses(np.concatenate(parts))
    audio = np.concatenate([audio * 10 ** ((LUFS - loudness(audio)) / 20), silence(0.8)])
    export(audio, args.mp3, args.title or Path(args.mp3).stem)
    print(f"Wrote {args.mp3}: {len(audio) / RATE:.1f} s of audio in {time.time() - start:.0f} s")


if __name__ == "__main__":
    main()
