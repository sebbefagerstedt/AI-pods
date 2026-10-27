#!/usr/bin/env bash
# Render every episode that has a script but no MP3, in order, and commit and push each MP3.
#
# Safe to stop and rerun: finished episodes are skipped, and finished segments come from
# .cache/, so a rerun picks up where the last one stopped. Problems the per-segment check
# finds are kept in .cache/render_all.log; list them with
#   grep -E "^== |take 1: [^e]" .cache/render_all.log
#
# tools/render_all.sh 08 renders the episode whose folder starts with 08 first, then the rest.
# TAKES=3 tools/render_all.sh retakes segments with problems (slower); the default, 1, doesn't.
set -euo pipefail
cd "$(dirname "$0")/.."
TAKES="${TAKES:-1}"
LOG=.cache/render_all.log
mkdir -p .cache

dirs=()
[[ -n "${1:-}" ]] && dirs+=(episodes/"$1"*/)
dirs+=(episodes/*/)

for dir in "${dirs[@]}"; do
  name=$(basename "$dir")
  mp3="$dir$name.mp3"
  [[ -f "${dir}script.md" && ! -f "$mp3" ]] || continue
  title=$(head -1 "${dir}script.md" | sed 's/^# *//')
  echo "== $name" | tee -a "$LOG"
  # Write to a temporary name, so an interrupted export never looks like a finished episode.
  .venv/bin/python tools/render.py "${dir}script.md" "$dir$name.partial.mp3" \
    --takes "$TAKES" --title "$title" 2>&1 | grep --line-buffered -v "HF Hub" | tee -a "$LOG"
  mv "$dir$name.partial.mp3" "$mp3"
  git add "$mp3"
  git commit -q -m "Render $title

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HxZ5z8Xp3ZYTQinoJMYX4d"
  for wait in 2 4 8 16; do git push -q origin HEAD && break || sleep "$wait"; done
done
echo "== all episodes rendered" | tee -a "$LOG"
