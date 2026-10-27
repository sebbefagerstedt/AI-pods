#!/usr/bin/env bash
# Retake the segments the batch render flagged, rebuild each episode's MP3 from the cache,
# and commit and push it. Safe to stop and rerun: finished episodes are listed in
# .cache/retakes.done and skipped.
set -euo pipefail
cd "$(dirname "$0")/.."
LOG=.cache/retakes.log
DONE=.cache/retakes.done
touch "$DONE"

while read -r name segs; do
  grep -qx "$name" "$DONE" && continue
  dir=episodes/$name
  title=$(head -1 "$dir/script.md" | sed 's/^# *//')
  echo "== $name: segments $segs" | tee -a "$LOG"
  # shellcheck disable=SC2086
  .venv/bin/python tools/retake.py "$dir/script.md" $segs </dev/null 2>&1 | grep -v "HF Hub" | tee -a "$LOG"
  .venv/bin/python tools/render.py "$dir/script.md" "$dir/$name.partial.mp3" --title "$title" </dev/null 2>&1 \
    | grep -v "HF Hub" | tee -a "$LOG"
  mv "$dir/$name.partial.mp3" "$dir/$name.mp3"
  git add "$dir/$name.mp3"
  git commit -q -m "Retake flagged segments of $title

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HxZ5z8Xp3ZYTQinoJMYX4d"
  for wait in 2 4 8 16; do git push -q origin HEAD && break || sleep "$wait"; done
  echo "$name" >> "$DONE"
done <<'LIST'
02-machine-learning 5
07-one-word-at-a-time 5 2
03-neural-networks 6 4
08-attention-is-all-you-need 6 7
11-press-enter 8 7
13-autocomplete-to-assistant 7
LIST
echo "== all retakes done" | tee -a "$LOG"
