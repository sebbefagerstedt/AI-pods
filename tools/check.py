#!/usr/bin/env python3
"""Check a render without listening to it.

Transcribes the audio with Whisper, lines the transcript up with the script to
find when each line is spoken, and reports lines that are missing or in the
wrong host's voice, plus stray sounds that sound like neither host:

    .venv/bin/python tools/check.py samples/sample.md samples/sample.mp3

The renderer runs the same check on each segment and retakes the ones that
fail, so a problem reported here survived several takes. Add --words to list
where the transcript's wording differs from the script, which also shows how
names were pronounced. Whisper mishears a few words in any recording, so look
for whole phrases missing or added, not single words.
"""

import argparse

from render import load_audio, parse, review, transcriber, voice_files, voice_matcher


def main():
    parser = argparse.ArgumentParser(description="Check a render against its script.")
    parser.add_argument("script", help="the script the audio was rendered from")
    parser.add_argument("audio", help="the rendered MP3")
    parser.add_argument("--voice", action="append", default=[], metavar="SPEAKER=FILE",
                        help="the recording a speaker was cloned from, if not voices/<name>.wav")
    parser.add_argument("--words", action="store_true", help="list where the wording differs from the script")
    args = parser.parse_args()

    turns = parse(args.script)
    score = voice_matcher(voice_files(turns, dict(v.split("=", 1) for v in args.voice)))
    problems, match, differences = review(turns, load_audio(args.audio, 16000), score, transcriber())
    print(f"{len(turns)} lines; the transcript matches {match:.0%} of the script's words.")
    print("\n".join(problems) or "Every line is there, in the right voice.")
    if args.words:
        print("\nDifferences (script -> heard):")
        for written, heard in differences:
            print(f"  {written or '-':45} -> {heard or '-'}")


if __name__ == "__main__":
    main()
