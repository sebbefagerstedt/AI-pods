#!/usr/bin/env bash
# Create .venv for VibeVoice text-to-speech, pinned to versions known to work.
# On Linux without an Nvidia card, the CPU build of PyTorch avoids gigabytes
# of CUDA libraries it can't use. Model weights download from Hugging Face on first use.
set -euo pipefail
cd "$(dirname "$0")/.."

uv venv --clear --python 3.12 .venv
if [ "$(uname)" = Linux ] && ! command -v nvidia-smi >/dev/null; then
    uv pip install --python .venv/bin/python torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
else  # a Mac, or Linux with an Nvidia card: the regular build supports their GPUs
    uv pip install --python .venv/bin/python torch==2.14.1
fi
uv pip install --python .venv/bin/python -r tools/requirements.txt
