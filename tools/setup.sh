#!/usr/bin/env bash
# Create .venv for VibeVoice text-to-speech, pinned to versions known to work.
# The CPU build of PyTorch avoids gigabytes of CUDA libraries this machine
# can't use. Model weights download from Hugging Face on first use.
set -euo pipefail
cd "$(dirname "$0")/.."

uv venv --clear --python 3.12 .venv
uv pip install --python .venv/bin/python torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
uv pip install --python .venv/bin/python -r tools/requirements.txt
