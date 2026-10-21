#!/usr/bin/env python3
"""Check a render without listening to it.

Transcribes the audio with Whisper, says which host's voice each stretch of
speech sounds like, and lists where the transcript differs from the script:

    .venv/bin/python tools/check.py samples/sample.md samples/sample.mp3

Voice similarity runs from 0 to 1; the right host typically scores above 0.85
and the other one near 0.5. A stretch of only a word or two scores lower for
both, so judge those by their neighbors. Whisper mishears a few words in any
recording, so look for whole phrases missing or added, not single words.
"""

import argparse
import difflib
import re
import subprocess

import numpy as np
import torch
from transformers import AutoFeatureExtractor, WavLMForXVector, pipeline
from transformers.utils import logging

from render import VOICES, parse

RATE = 16000  # what Whisper and the speaker model expect


def load(path):
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(RATE), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(pcm, dtype=np.float32)


def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())


def main():
    parser = argparse.ArgumentParser(description="Transcribe a render and check who speaks each part.")
    parser.add_argument("script", help="the script the audio was rendered from")
    parser.add_argument("audio", help="the rendered MP3")
    parser.add_argument("--voice", action="append", default=[], metavar="SPEAKER=WAV",
                        help="the recordings the render cloned, if not the defaults")
    args = parser.parse_args()

    voices = VOICES | dict(v.split("=", 1) for v in args.voice)
    turns = parse(args.script, voices)
    logging.set_verbosity_error()
    logging.disable_progress_bar()
    extractor = AutoFeatureExtractor.from_pretrained("microsoft/wavlm-base-plus-sv")
    speaker_model = WavLMForXVector.from_pretrained("microsoft/wavlm-base-plus-sv").eval()

    def embed(audio):
        with torch.inference_mode():
            inputs = extractor(audio, sampling_rate=RATE, return_tensors="pt")
            return torch.nn.functional.normalize(speaker_model(**inputs).embeddings[0], dim=-1)

    references = {speaker: embed(load(voices[speaker])) for speaker in sorted({s for s, _ in turns})}
    audio = load(args.audio)
    asr = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")
    chunks = asr({"raw": audio, "sampling_rate": RATE}, return_timestamps=True)["chunks"]
    for chunk in chunks:
        start, end = chunk["timestamp"]
        end = end or len(audio) / RATE
        if end - start < 0.3:
            continue
        voice = embed(audio[int(start * RATE) : int(end * RATE)])
        scores = {speaker: float(voice @ ref) for speaker, ref in references.items()}
        closest = max(scores, key=scores.get)
        print(f"{start:6.1f}s  {closest:7} " + " ".join(f"{s}={v:.2f}" for s, v in scores.items())
              + f"  {chunk['text'].strip()}")

    written = words(" ".join(text for _, text in turns))
    heard = words(" ".join(chunk["text"] for chunk in chunks))
    matcher = difflib.SequenceMatcher(None, written, heard, autojunk=False)
    print(f"\nTranscript matches {matcher.ratio():.0%} of the script. Differences:")
    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op != "equal":
            print(f"  script: {' '.join(written[i1:i2]) or '-':45} heard: {' '.join(heard[j1:j2]) or '-'}")


if __name__ == "__main__":
    main()
