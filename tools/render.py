#!/usr/bin/env python3
"""Turn a two-host script into a podcast MP3 with VibeVoice.

VibeVoice performs the whole conversation at once, so the hosts react to each
other the way people talking do. Each host's voice is cloned from a short
recording: voices/<name>.wav, unless --voice says otherwise.

Every paragraph of the script starts with the speaker's name in capitals,
plain or bold. Headings (lines starting with #) are skipped:

    FRANK: Think about how a kid learns what a cat is.

    **ALICE:** Wait, and that works for computers?

Set up the venv with tools/setup.sh, then:

    .venv/bin/python tools/render.py samples/sample.md samples/sample.mp3
    .venv/bin/python tools/render.py script.md out.mp3 --voice ALICE=voices/maya.wav

It renders about 3 minutes of script at a time, about 5 times slower than real
time on 4 CPUs. VibeVoice now and then puts a line in the wrong voice, garbles
it or adds a stray sound, so each segment is transcribed and checked, and
retaken with a new seed if anything is off; --takes 1 skips the retakes.
It uses an Nvidia graphics card or Apple silicon when there is one. Finished segments are cached in
.cache/, so a render that gets interrupted picks up where it stopped.
"""

import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import warnings
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

warnings.filterwarnings("ignore")  # deprecation noise from torch and transformers

import numpy as np
import soundfile as sf
import torch
from transformers import (AutoFeatureExtractor, AutoModelForTextToWaveform, AutoProcessor, WavLMForXVector, pipeline,
                          set_seed)
from transformers.utils import logging

logging.set_verbosity_error()
logging.disable_progress_bar()

ROOT = Path(__file__).resolve().parent.parent
MODEL = "vibevoice/VibeVoice-1.5B-hf"
SPEAKER_MODEL = "microsoft/wavlm-base-plus-sv"  # tells the hosts apart by their voices
ASR_MODEL = "openai/whisper-small.en"  # hears whether each line came out right
RATE = 24000  # VibeVoice's sample rate
SEGMENT_CHARS = 3000  # about 3 minutes of speech per generation
TAKES = 3  # tries per segment before settling for the take with the fewest problems
LONGEST_PAUSE = 0.7  # seconds; the model sometimes leaves longer gaps between turns
MIN_GAP = 0.15  # seconds of quiet that end a stretch of speech
MIN_VOICE = 0.5  # seconds of audio the speaker model needs
CONFIDENT = 0.2  # how much closer a stretch must sound to one voice than the other to count
LUFS = -19  # Apple asks for -16; a mono file plays 3 dB louder on two speakers
PEAK = -2.5  # limiter ceiling in dBFS, leaving room for MP3 overshoot under Apple's -1
CACHE = ROOT / ".cache" / "segments"
LABEL = re.compile(r"\**([A-Z]+):\**\s*(.+)")


def parse(path):
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
        turns.append((match[1], match[2].replace("*", "")))
    return turns


def voice_files(turns, overrides):
    """Map each speaker in the script to the recording their voice is cloned from."""
    voices = {}
    for speaker in sorted({speaker for speaker, _ in turns}):
        path = Path(overrides.get(speaker) or ROOT / "voices" / f"{speaker.lower()}.wav")
        if not path.exists():
            sys.exit(f"No voice for {speaker}: add voices/{speaker.lower()}.wav or pass --voice {speaker}=FILE")
        voices[speaker] = path
    return voices


def segments(turns):
    """Group turns into runs of about SEGMENT_CHARS, each generated in one go."""
    groups = [[]]
    for turn in turns:
        if groups[-1] and sum(len(text) for _, text in groups[-1]) + len(turn[1]) > SEGMENT_CHARS:
            groups.append([])
        groups[-1].append(turn)
    return groups


def load_audio(path, rate=RATE):
    """Read any audio file as mono samples at `rate`."""
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(rate), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(pcm, dtype=np.float32).copy()


def cache_path(segment, voices, seed):
    """Where a segment's audio is cached; changing its text, a voice or the seed misses."""
    used = sorted({speaker for speaker, _ in segment})
    voice_hashes = [hashlib.sha1(Path(voices[speaker]).read_bytes()).hexdigest() for speaker in used]
    key = json.dumps([MODEL, seed, segment, voice_hashes])
    return CACHE / f"{hashlib.sha1(key.encode()).hexdigest()}.wav"


def device():
    """The fastest place to run VibeVoice here, and the number format to run it in."""
    if torch.cuda.is_available():
        return "cuda", torch.bfloat16
    if torch.backends.mps.is_available():  # Apple silicon
        return "mps", torch.float32
    return "cpu", torch.bfloat16  # fast on CPUs with AMX, slow but working on others


def synthesize(segment, voices, seed, processor, model):
    """Perform one segment of the conversation, cloning each speaker's voice."""
    roles, conversation = {}, []
    for speaker, text in segment:
        content = [{"type": "text", "text": text}]
        if speaker not in roles:  # number speakers by first appearance; give each its voice once
            roles[speaker] = str(len(roles))
            content.append({"type": "audio", "audio": load_audio(voices[speaker])})
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


def quiet_frames(audio, rate):
    """Split audio into 20 ms frames; return the frame length and which frames are quiet."""
    n = int(0.02 * rate)
    db = 20 * np.log10(np.abs(audio[: len(audio) // n * n]).reshape(-1, n).max(axis=1) + 1e-9)
    return n, db < np.percentile(db, 95) - 35


def cap_pauses(audio):
    """Shorten silences longer than LONGEST_PAUSE to that length, cutting out their middle."""
    n, quiet = quiet_frames(audio, RATE)
    quiet = np.append(quiet, False)
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


def stretches(audio, rate):
    """Split audio at pauses of at least MIN_GAP into (start, end) sample ranges of speech."""
    n, quiet = quiet_frames(audio, rate)
    spans, start, last = [], None, 0
    for i, q in enumerate(quiet):
        if not q:
            if start is None:
                start = i
            last = i
        elif start is not None and (i - last) * 0.02 >= MIN_GAP:
            spans.append((start * n, (last + 1) * n))
            start = None
    if start is not None:
        spans.append((start * n, (last + 1) * n))
    return [(a, b) for a, b in spans if b - a >= 0.3 * rate]


def voice_matcher(voices):
    """Return a function that scores 16 kHz audio against each speaker's voice, from 0 to 1.

    It returns None for audio too short to tell.
    """
    extractor = AutoFeatureExtractor.from_pretrained(SPEAKER_MODEL)
    model = WavLMForXVector.from_pretrained(SPEAKER_MODEL).eval()

    def embed(audio):
        with torch.inference_mode():
            inputs = extractor(audio, sampling_rate=16000, return_tensors="pt")
            return torch.nn.functional.normalize(model(**inputs).embeddings[0], dim=-1)

    references = {speaker: embed(load_audio(path, 16000)) for speaker, path in voices.items()}

    def score(audio):
        if len(audio) < MIN_VOICE * 16000:
            return None
        voice = embed(audio)
        return {speaker: float(voice @ ref) for speaker, ref in references.items()}

    return score


def closest(scores):
    """The speaker a stretch clearly sounds like, or None if it's too short or too close to call."""
    if not scores:
        return None
    ranked = sorted(scores, key=scores.get, reverse=True)
    if len(ranked) == 1 or scores[ranked[0]] - scores[ranked[1]] >= CONFIDENT:
        return ranked[0]
    return None


def words(text):
    """Lowercase words without punctuation, for comparing a script with a transcript."""
    return re.findall(r"[a-z0-9']+", text.lower())


def transcriber():
    """Return a function that turns 16 kHz audio into (word, start, end) tuples."""
    asr = pipeline("automatic-speech-recognition", model=ASR_MODEL, chunk_length_s=30)

    def transcribe(audio):
        chunks = asr({"raw": audio, "sampling_rate": 16000}, return_timestamps="word")["chunks"]
        return [(word, chunk["timestamp"][0], chunk["timestamp"][1] or chunk["timestamp"][0])
                for chunk in chunks for word in words(chunk["text"])]

    return transcribe


def review(turns, audio16, score, transcribe, first_line=1):
    """Find what went wrong in a render: lines missing or in the wrong voice, and odd sounds.

    Lines a Whisper transcript up with the script word by word to find when each
    line is spoken, then checks whose voice it's in. Returns the problems, how
    much of the script's wording the transcript matches, and where they differ.
    """
    heard = transcribe(audio16)
    written = [(word, i) for i, (_, text) in enumerate(turns) for word in words(text)]
    matcher = difflib.SequenceMatcher(None, [w for w, _ in written], [w for w, _, _ in heard], autojunk=False)
    spoken = defaultdict(list)  # line -> (start, end) of each of its words that was heard
    for a, b, size in matcher.get_matching_blocks():
        for k in range(size):
            _, start, end = heard[b + k]
            # Whisper often runs a word's end on over the pause after it, so cap it
            spoken[written[a + k][1]].append((start, min(end, start + 0.5)))
    problems = []
    for i, (speaker, text) in enumerate(turns):
        line, total = f"line {first_line + i} ({speaker})", len(words(text))
        if total >= 5 and len(spoken[i]) < 0.6 * total:
            problems.append(f"{line} mostly missing: heard {len(spoken[i])} of {total} words")
        elif spoken[i]:
            start, end = spoken[i][0][0], spoken[i][-1][1]
            voice = closest(score(audio16[int(start * 16000) : int(end * 16000)]))
            if voice and voice != speaker:
                problems.append(f"{line} came out in {voice}'s voice")
    times = [t for line in spoken.values() for t in line]
    for start, end in stretches(audio16, 16000):
        start, end = start / 16000, end / 16000
        scripted = sum(max(0, min(e, end) - max(s, start)) for s, e in times)
        if scripted < 0.3 * (end - start):
            scores = score(audio16[int(start * 16000) : int(end * 16000)])
            if scores and max(scores.values()) < 0.6:
                problems.append(f"odd sound at {start:.1f} s, like neither host")
    differences = [(" ".join(w for w, _ in written[i1:i2]), " ".join(w for w, _, _ in heard[j1:j2]))
                   for op, i1, i2, j1, j2 in matcher.get_opcodes() if op != "equal"]
    return problems, matcher.ratio(), differences


def to_16k(audio):
    """Resample to 16 kHz, what Whisper and the speaker model expect."""
    with as_wav(audio) as wav:
        return load_audio(wav, 16000)


def level_speakers(audio, score):
    """Bring each host to the target loudness, telling who speaks each stretch by voice.

    Clones can come out a dB or two apart. The gain only changes in the pauses
    between stretches.
    """
    audio16 = to_16k(audio)
    spans = stretches(audio, RATE)
    labels = [closest(score(audio16[a * 2 // 3 : b * 2 // 3])) for a, b in spans]
    known = [label for label in labels if label]
    if not known:
        return audio * 10 ** ((LUFS - loudness(audio)) / 20)
    previous = known[0]
    for i, label in enumerate(labels):  # a stretch too short to tell goes with the one before
        labels[i] = previous = label or previous
    gain = {}
    for speaker in set(labels):
        lufs = loudness(np.concatenate([audio[a:b] for (a, b), label in zip(spans, labels) if label == speaker]))
        gain[speaker] = 10 ** ((LUFS - lufs) / 20) if np.isfinite(lufs) else 1.0
    points = [x for span in spans for x in span]
    gains = [gain[label] for label in labels for _ in range(2)]
    return audio * np.interp(np.arange(len(audio)), points, gains).astype(np.float32)


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
    """Catch the peaks the loudness gain pushed too high, and encode a mono MP3.

    The limiter shaves a little loudness off, so measure how much and make it up first.
    """
    limiter = f"alimiter=limit={10 ** (PEAK / 20):.3f}:level=disabled:latency=1"
    with as_wav(audio) as wav:
        log = ffmpeg("-i", wav, "-af", f"{limiter},loudnorm=print_format=json", "-f", "null", "-")
    shortfall = LUFS - float(json.loads(log[log.rindex("{") :])["input_i"])
    with as_wav(audio * 10 ** (shortfall / 20)) as wav:
        ffmpeg("-y", "-i", wav, "-af", limiter, "-ar", "44100", "-ac", "1",
               "-c:a", "libmp3lame", "-b:a", "96k", "-id3v2_version", "3",
               "-metadata", f"title={title}", str(path))


def main():
    parser = argparse.ArgumentParser(description="Render a two-host script to MP3 with VibeVoice.")
    parser.add_argument("script", help="Markdown script, one speaker-labeled paragraph per turn")
    parser.add_argument("mp3", help="output file")
    parser.add_argument("--voice", action="append", default=[], metavar="SPEAKER=FILE",
                        help="clone a speaker's voice from this recording instead of voices/<name>.wav")
    parser.add_argument("--seed", type=int, default=42, help="change it to get a different take")
    parser.add_argument("--takes", type=int, default=TAKES,
                        help=f"tries per segment when the check finds a problem (default {TAKES}; 1 is fastest)")
    parser.add_argument("--title", help="MP3 title tag (default: output file name)")
    args = parser.parse_args()

    turns = parse(args.script)
    voices = voice_files(turns, dict(v.split("=", 1) for v in args.voice))
    groups = segments(turns)
    score = voice_matcher(voices)
    start = time.time()
    parts, processor, model, transcribe, first_line = [], None, None, None, 1
    for n, segment in enumerate(groups, 1):
        path = cache_path(segment, voices, args.seed)
        if not path.exists():
            if model is None:
                processor = AutoProcessor.from_pretrained(MODEL)
                where, dtype = device()
                model = AutoModelForTextToWaveform.from_pretrained(MODEL, dtype=dtype).to(where).eval()
                transcribe = transcriber()
            best = None
            for take in range(args.takes):
                audio = synthesize(segment, voices, args.seed + take, processor, model)
                problems = review(segment, to_16k(audio), score, transcribe, first_line)[0]
                print(f"[{n}/{len(groups)}] take {take + 1}: {'; '.join(problems) or 'every line checks out'}",
                      flush=True)
                if best is None or len(problems) < len(best[1]):
                    best = audio, problems
                if not problems:
                    break
            CACHE.mkdir(parents=True, exist_ok=True)
            partial = path.with_suffix(".partial.wav")
            sf.write(partial, best[0], RATE)
            partial.replace(path)
        parts.append(sf.read(path, dtype="float32")[0])
        first_line += len(segment)
        print(f"[{n}/{len(groups)}] {len(parts[-1]) / RATE:.0f} s of audio, {time.time() - start:.0f} s so far",
              flush=True)

    audio = level_speakers(cap_pauses(np.concatenate(parts)), score)
    audio = np.concatenate([audio, silence(0.8)])
    export(audio, args.mp3, args.title or Path(args.mp3).stem)
    print(f"Wrote {args.mp3}: {len(audio) / RATE:.1f} s of audio in {time.time() - start:.0f} s")


if __name__ == "__main__":
    main()
