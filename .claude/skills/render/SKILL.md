---
name: render
description: Render episode scripts to MP3, restart a render that stopped at the 2-hour limit, check a finished episode, or retake flagged segments. Use whenever the listener asks to render, re-render, restart, check or retake an episode.
---

# Rendering episodes

## Batch renders in the cloud

- Run `tools/render_all.sh` as a background Bash job with the longest timeout (7200000 ms). It renders every episode that has a script and no MP3, in order, with `--takes 1` (no retakes; problems are only logged), then commits and pushes each MP3. `tools/render_all.sh s2-03` renders the episode whose folder starts with `s2-03` first, then the rest.
- A background job stops after 2 hours. The listener has asked for it to be started again each time, the same way, until the log ends with "== all episodes rendered". It resumes from the cache. The listener wants to keep tokens low, so keep these check-ins short: don't read scripts, don't run `check.py`, just restart, and say in one line which episode it's on (`tail -3 .cache/render_all.log`).
- At the end, list the problem lines with `grep -E "^== |take 1: [^e]" .cache/render_all.log` for the listener, who decides which segments, if any, to redo. The listener will listen anyway and doesn't need perfection.
- To retake segments, list them as `episode-folder segment...` lines in a file like `tools/retakes/first.txt` and run `tools/retake_all.sh` on it, also as a background job. It gives each segment up to 2 new takes with `tools/retake.py`, keeps the best (the cached one included), rebuilds each MP3 from the cache and pushes it.
- To re-render an episode after changing its script, delete its MP3 and run `tools/render_all.sh NN` (only the changed segments render).

## The renderer and the check

- Render with `.venv/bin/python tools/render.py SCRIPT.md OUT.mp3`, adding `--voice ALICE=voices/maya.wav` to use another recording `--seed 7` for different takes, or `--takes 1` to skip retakes (about half the time). It uses an Nvidia card or Apple silicon when there is one (untested). It runs about 4.7 times slower than real time, using the CPU's bfloat16 (AMX) support, so a 20-minute episode takes about 1.5 hours, more if segments need retakes: run it in the background. The first render after the container restarts is slower, since the model has to be read from disk again. It renders about 3 minutes of script at a time and caches each finished segment in `.cache/`, so an interrupted render resumes where it stopped. The checks use `openai/whisper-small.en` and `microsoft/wavlm-base-plus-sv`, also downloaded on first use.
- Output is a mono MP3 at 44.1 kHz and 96 kbps, about 0.7 MB a minute. Pauses longer than 0.7 s are shortened. Each host is leveled to -19 LUFS; the renderer tells them apart by voice, since clones can come out a dB or two apart. A mono file plays 3 dB louder on two speakers, so -19 LUFS matches Apple's -16 LUFS target. A limiter keeps true peaks under Apple's -1 dBTP.
- Nobody can listen during a session, so also run `tools/check.py SCRIPT.md OUT.mp3` on the finished episode. It runs the same check over the whole file and lists any line that's missing or in the wrong voice; `--words` lists where the wording differs, which shows how names came out. On a whole episode it takes about as long as the audio, so run it in the background and alone. Whisper sometimes gets stuck repeating "thank you" (or "we'll see you in the next video") over a stretch, which shows up as a missing line; transcribe that stretch on its own before believing it. On episode 9 the whole-file check flagged four lines as mostly missing that were all there: Whisper loses its place on long files. Re-running `review` on the cached segment that holds the line (`.cache/segments/`, found with `segments` and `cache_path`) settles it.
