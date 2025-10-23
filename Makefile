.PHONY: install run-api run-ui test docker-build docker-run

install:
	python3 -m pip install -U pdm
	pdm install

run-api:
	pdm run uvicorn app.main:app --reload --port 8000

run-ui:
	pdm run streamlit run ui/streamlit_dashboard.py

docker-build:
	docker build -t agentzarvis:local .

docker-run:
	docker run --rm -p 8000:8000 agentzarvis:local
