#!/usr/bin/env bash
set -euo pipefail

PY=${PYTHON:-python3}

# Create venv
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment at .venv"
  ${PY} -m venv .venv
fi

# Activate
source .venv/bin/activate

# Upgrade pip & install prereqs
python -m pip install -U pip wheel

# Install requirements
pip install -r requirements.txt

echo "✅ venv ready. Activate with: source .venv/bin/activate"
