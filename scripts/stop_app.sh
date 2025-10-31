#!/usr/bin/env bash
# Simple helper to kill uvicorn if left running
pkill -f "uvicorn app.main:app" || true
echo "🛑 Stopped uvicorn (if running)."
