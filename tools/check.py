#!/usr/bin/env python3
"""Check a render without listening to it.

Splits the audio at pauses, says which host's voice each stretch sounds like
and transcribes it with Whisper, then compares the result with the script:
the order in which the hosts speak, and the words.

    .venv/bin/python tools/check.py samples/sample.md samples/sample.mp3

Voice similarity runs from 0 to 1; the right host typically scores above 0.85
and the other one near 0.5. A stretch of only a word or two can score close to
both; it's marked "?" and left out of the speaking order. Whisper mishears a
few words in any recording, and can miss a soft word at the edge of a stretch,
so look for whole phrases missing or added, not single words.
"""

import argparse
import difflib
import itertools
import re

from transformers import pipeline

from render import VOICES, closest, load_audio, parse, stretches, voice_matcher

RATE = 16000  # what Whisper and the speaker model expect
PAD = 0.1  # seconds kept around each stretch, so soft first and last words aren't clipped


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
    score = voice_matcher({speaker: voices[speaker] for speaker in sorted({s for s, _ in turns})})
    asr = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")
    audio = load_audio(args.audio, RATE)
    order, heard = [], []
    for start, end in stretches(audio, RATE):
        clip = audio[max(start - int(PAD * RATE), 0) : end + int(PAD * RATE)]
        heard.append(asr({"raw": clip, "sampling_rate": RATE}, return_timestamps=True)["text"].strip())
        scores = score(clip)
        speaker = closest(scores)
        if speaker:
            order.append(speaker)
        detail = " ".join(f"{s}={v:.2f}" for s, v in scores.items()) if scores else "too short to tell"
        print(f"{start / RATE:6.1f}s  {speaker or '?':7} {detail}  {heard[-1]}")

    expected = [speaker for speaker, _ in itertools.groupby(s for s, _ in turns)]
    spoken = [speaker for speaker, _ in itertools.groupby(order)]
    if spoken == expected:
        print(f"\nThe hosts speak in the script's order ({len(expected)} turns).")
    else:
        print(f"\nThe speaking order differs from the script:\n  script: {' '.join(expected)}\n  heard:  {' '.join(spoken)}")

    written, said = words(" ".join(text for _, text in turns)), words(" ".join(heard))
    matcher = difflib.SequenceMatcher(None, written, said, autojunk=False)
    print(f"Transcript matches {matcher.ratio():.0%} of the script. Differences:")
    for op, i1, i2, j1, j2 in matcher.get_opcodes():
        if op != "equal":
            print(f"  script: {' '.join(written[i1:i2]) or '-':45} heard: {' '.join(said[j1:j2]) or '-'}")


if __name__ == "__main__":
    main()
