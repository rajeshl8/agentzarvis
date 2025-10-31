# =============================
# AgentZarvis Makefile (auto-activate cross-platform)
# =============================

# Detect OS
UNAME_S := $(shell uname 2>/dev/null)
IS_WIN := 0
ifeq ($(OS),Windows_NT)
  IS_WIN := 1
endif
ifneq (,$(findstring MINGW,$(UNAME_S)))
  IS_WIN := 1
endif
ifneq (,$(findstring MSYS,$(UNAME_S)))
  IS_WIN := 1
endif

# Common paths
ifeq ($(IS_WIN),1)
  PY_SYS := py -3.11
  VENV_PY := .venv\Scripts\python.exe
  ACTIVATE := .venv\Scripts\Activate.ps1
  PIP := .venv\Scripts\pip.exe
else
  PY_SYS := python3
  VENV_PY := .venv/bin/python
  ACTIVATE := .venv/bin/activate
  PIP := .venv/bin/pip
endif

.PHONY: setup run-api run-ui run-app stop clean

# ------------------------------------------------------------
# Setup: create venv, install deps, and activate automatically
# ------------------------------------------------------------
setup:
ifeq ($(IS_WIN),1)
	@echo "🚀 Creating or updating venv (Windows)..."
	@if not exist .venv ( $(PY_SYS) -m venv .venv )
	@echo "📦 Installing dependencies..."
	@$(VENV_PY) -m pip install -U pip wheel
	@$(PIP) install -r requirements.txt
	@echo "✅ Setup complete."
	@echo "💡 To activate venv manually next time:"
	@echo "   PowerShell: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\\$(ACTIVATE)"
	@echo "   CMD: .venv\\Scripts\\activate.bat"
	@echo "⚡ Activating venv now for this session..."
	@powershell -NoLogo -NoExit -Command "Set-ExecutionPolicy -Scope Process Bypass; .\\$(ACTIVATE)"
else
	@echo "🚀 Creating or updating venv (Unix/macOS)..."
	@test -d .venv || $(PY_SYS) -m venv .venv
	@echo "📦 Installing dependencies..."
	@$(VENV_PY) -m pip install -U pip wheel
	@$(PIP) install -r requirements.txt
	@echo "✅ Setup complete."
	@echo "💡 To activate venv manually next time: source $(ACTIVATE)"
	@echo "⚡ Activating venv now for this session..."
	@bash -c "source $(ACTIVATE); exec bash"
endif

# ------------------------------------------------------------
# Run backend API
# ------------------------------------------------------------
run-api:
	@$(VENV_PY) -m uvicorn app.main:app --reload --port 8000

# ------------------------------------------------------------
# Run Streamlit UI
# ------------------------------------------------------------
run-ui:
	@$(VENV_PY) -m streamlit run ui/streamlit_dashboard.py

# ------------------------------------------------------------
# Run both together
# ------------------------------------------------------------
run-app:
ifeq ($(IS_WIN),1)
	@start cmd /k "$(VENV_PY) -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
	@$(VENV_PY) -m streamlit run ui\streamlit_dashboard.py
else
	@bash -lc '$(VENV_PY) -m uvicorn app.main:app --host 0.0.0.0 --port 8000 & echo $$! > .uv.pid; \
	  trap "kill -9 $$(cat .uv.pid) 2>/dev/null || true; rm -f .uv.pid" INT TERM EXIT; \
	  $(VENV_PY) -m streamlit run ui/streamlit_dashboard.py'
endif

# ------------------------------------------------------------
# Stop and clean
# ------------------------------------------------------------
stop:
ifeq ($(IS_WIN),1)
	@taskkill /F /IM python.exe /FI "WINDOWTITLE eq uvicorn*" 2>nul || echo "No uvicorn process found."
else
	@pkill -f "uvicorn app.main:app" || true
endif

clean:
ifeq ($(IS_WIN),1)
	@if exist .venv rmdir /s /q .venv
else
	@rm -rf .venv __pycache__ .pytest_cache .streamlit
endif
	@echo "🧹 Clean complete."
