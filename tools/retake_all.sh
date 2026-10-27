#!/usr/bin/env bash
# Check and retake the segments listed in LISTFILE (lines of "episode-folder segment..."),
# rebuild each episode's MP3 from the cache, and commit and push it if it changed.
# Safe to stop and rerun: finished episodes are listed in .cache/<list name>.done and skipped.
#   tools/retake_all.sh tools/retakes/second.txt
set -euo pipefail
cd "$(dirname "$0")/.."
LIST="$1"
LOG=.cache/retakes.log
DONE=.cache/$(basename "$LIST" .txt).done
touch "$DONE"

while read -r name segs; do
  grep -qx "$name" "$DONE" && continue
  dir=episodes/$name
  title=$(head -1 "$dir/script.md" | sed 's/^# *//')
  echo "== $name: segments $segs" | tee -a "$LOG"
  # shellcheck disable=SC2086
  .venv/bin/python tools/retake.py "$dir/script.md" $segs </dev/null 2>&1 | grep --line-buffered -v "HF Hub" | tee -a "$LOG"
  .venv/bin/python tools/render.py "$dir/script.md" "$dir/$name.partial.mp3" --title "$title" </dev/null 2>&1 \
    | grep --line-buffered -v "HF Hub" | tee -a "$LOG"
  mv "$dir/$name.partial.mp3" "$dir/$name.mp3"
  git add "$dir/$name.mp3"
  git diff --cached --quiet && { echo "$name" >> "$DONE"; continue; }
  git commit -q -m "Retake flagged segments of $title

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HxZ5z8Xp3ZYTQinoJMYX4d"
  for wait in 2 4 8 16; do git push -q origin HEAD && break || sleep "$wait"; done
  echo "$name" >> "$DONE"
done < "$LIST"
echo "== all retakes done: $LIST" | tee -a "$LOG"
