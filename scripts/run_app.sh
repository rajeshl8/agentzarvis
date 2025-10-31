#!/usr/bin/env bash
set -euo pipefail

# Ensure venv is active
if [ -z "${VIRTUAL_ENV:-}" ]; then
  if [ -d ".venv" ]; then
    source .venv/bin/activate
  else:
    echo "No .venv found. Run: make setup"
    exit 1
  fi
fi

# Start API in background
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
API_PID=$!
echo "API started (pid $API_PID) on http://127.0.0.1:8000"

# Start UI in foreground (Ctrl+C stops UI; trap stops API)
trap "echo Stopping API ($API_PID); kill $API_PID 2>/dev/null || true" INT TERM
streamlit run ui/streamlit_dashboard.py
