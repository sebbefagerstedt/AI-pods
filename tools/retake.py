"""Retake chosen segments of an episode that's already rendered, keeping the best take.

    .venv/bin/python tools/retake.py episodes/08-attention-is-all-you-need/script.md 6 7

Segment numbers are the [n/N] ones in the render log. Each segment gets up to --takes new
takes with new seeds; the take with the fewest problems, the cached one included, replaces
the cached audio. Rerun render.py on the script afterwards to rebuild the MP3 from the cache.
"""
import argparse

import soundfile as sf
from transformers import AutoModelForTextToWaveform, AutoProcessor

from render import (MODEL, RATE, cache_path, device, parse, review, segments, synthesize, to_16k, transcriber,
                    voice_files, voice_matcher)


def main():
    parser = argparse.ArgumentParser(description="Retake segments of a rendered episode.")
    parser.add_argument("script")
    parser.add_argument("segment", type=int, nargs="+", help="segment numbers, as in the render log")
    parser.add_argument("--takes", type=int, default=2, help="new takes per segment (default 2)")
    parser.add_argument("--seed", type=int, default=42, help="the seed the episode was rendered with")
    args = parser.parse_args()

    turns = parse(args.script)
    voices = voice_files(turns, {})
    groups = segments(turns)
    score = voice_matcher(voices)
    transcribe = transcriber()
    processor = AutoProcessor.from_pretrained(MODEL)
    where, dtype = device()
    model = AutoModelForTextToWaveform.from_pretrained(MODEL, dtype=dtype).to(where).eval()
    for n in args.segment:
        segment = groups[n - 1]
        first_line = 1 + sum(len(g) for g in groups[: n - 1])
        path = cache_path(segment, voices, args.seed)
        audio = sf.read(path, dtype="float32")[0]
        best = audio, review(segment, to_16k(audio), score, transcribe, first_line)[0]
        print(f"[{n}] cached: {'; '.join(best[1]) or 'every line checks out'}", flush=True)
        # The render tried seeds seed, seed + 1, ... for its takes; start past the three it may have used
        for take in range(args.takes):
            if not best[1]:
                break
            audio = synthesize(segment, voices, args.seed + 3 + take, processor, model)
            problems = review(segment, to_16k(audio), score, transcribe, first_line)[0]
            print(f"[{n}] retake {take + 1}: {'; '.join(problems) or 'every line checks out'}", flush=True)
            if len(problems) < len(best[1]):
                best = audio, problems
                partial = path.with_suffix(".partial.wav")
                sf.write(partial, audio, RATE)
                partial.replace(path)
        print(f"[{n}] kept: {'; '.join(best[1]) or 'every line checks out'}", flush=True)


if __name__ == "__main__":
    main()
