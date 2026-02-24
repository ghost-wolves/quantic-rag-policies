# Quantic Project 05 - Local RAG Policies Assistant

Local-only Retrieval-Augmented Generation (RAG) web app that answers questions over a small corpus of policy/procedure documents with citations, plus automated tests, evaluation metrics, and GitHub Actions CI.

## LOCAL SETUP
### 1) Create venv + install dependencies
   python -m venv .venv
   # Git Bash (Windows):
   source .venv/Scripts/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

### 2) Configure environment variables
   cp .env.example .env
   Then edit .env and set your API key(s). Never commit .env.

### 3) Build index (to be implemented)
   python -m src.ingest

### 4) Run app (to be implemented)
   python -m src.app

### 5) Run tests
   pytest -q

### 6) Run evaluation (to be implemented)
   python -m eval.run_eval

## REPO STRUCTURE
- data/raw/        — source documents
- data/processed/  — cleaned/chunked artifacts (ignored by git)
- vectorstore/     — local vector DB persistence (ignored by git)
- src/             — application code
- tests/           — pytest tests
- eval/            — evaluation questions + scripts