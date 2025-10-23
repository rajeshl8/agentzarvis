# AgentZarvis

**AgentZarvis** is your personalized AI PA — plans, prioritizes, and executes your day.
Built for the NVIDIA–AWS hackathon with a simple two-track team workflow (Backend & UI).

## Quickstart (Local)

```bash
# install pdm if not present
python3 -m pip install -U pdm

# install deps
pdm install

# terminal A: run API
pdm run api

# terminal B: run UI
pdm run ui
```

Open the Streamlit app, edit the sample inputs, and click **Generate Brief**.

## API

- `GET /health` — health check
- `POST /brief` — generates a Daily Executive Brief from the provided JSON payload  
  Payload matches `docs/api_contract.md`.

## Project Layout

```
agentzarvis/
  app/
    main.py
    orchestrator.py
    agents/
      inbox_agent.py
      planner_agent.py
      meeting_agent.py
    rag/
      retrieval_nim.py
      s3_indexer.py
    prompts/
      inbox.md
      planner.md
      meeting.md
  ui/
    streamlit_dashboard.py
    mock_response.json
  data_samples/
    emails.json
    calendar.ics
    meeting.txt
  deploy/
    eks-deployment.yaml
    eks-service.yaml
  docs/
    api_contract.md
  README.md
  pyproject.toml
```

## Built With

**Python**, **FastAPI**, **Streamlit**, **Amazon EKS**, **Amazon S3**, **NVIDIA NIM microservices** (Llama-3 1-Nemotron-Nano-8B + Retrieval Embedding NIM), **Docker**, **Kubernetes**, **JSON**, **ICS**, **REST APIs**, **AWS CLI**, **Git**

## Two-Person Workflow

- **Track A — Backend/Agents:** build `/brief` endpoint + agents.  
- **Track B — UI/DevOps:** build Streamlit against mock JSON, then switch to API.

See `docs/api_contract.md` for the frozen request/response shapes.
