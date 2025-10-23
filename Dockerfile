FROM python:3.11-slim

WORKDIR /app

# System deps (optional: build tools)
RUN apt-get update && apt-get install -y --no-install-recommends     curl ca-certificates build-essential  && rm -rf /var/lib/apt/lists/*

# Copy project metadata first for layer caching
COPY pyproject.toml ./

# Install pdm and project deps (no venv)
RUN pip install -U pip pdm && pdm config python.use_venv false && pdm install --prod --no-editable

# Copy the rest of the source
COPY . .

EXPOSE 8000

# Default command: run FastAPI API
CMD ["pdm","run","uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
