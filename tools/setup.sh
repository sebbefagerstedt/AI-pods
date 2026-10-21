#!/usr/bin/env bash
# Create .venv with Kokoro text-to-speech, pinned to versions known to work.
# Kokoro needs Python 3.10-3.12, and the CPU build of PyTorch avoids
# gigabytes of CUDA libraries this machine can't use.
set -euo pipefail
cd "$(dirname "$0")/.."

uv venv --clear --python 3.12 .venv
uv pip install --python .venv/bin/python torch==2.14.1 --index-url https://download.pytorch.org/whl/cpu
uv pip install --python .venv/bin/python -r tools/requirements.txt

# misaki (Kokoro's text front-end) needs this spaCy model, and would try to
# fetch it with pip, which the uv venv lacks. GitHub first, then Hugging Face.
uv pip install --python .venv/bin/python "en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl" ||
  uv pip install --python .venv/bin/python "en_core_web_sm @ https://huggingface.co/spacy/en_core_web_sm/resolve/main/en_core_web_sm-any-py3-none-any.whl"
