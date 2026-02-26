# Quantic Project 05 - Local RAG Policies Assistant

Local-only Retrieval-Augmented Generation (RAG) web app that answers questions over a small corpus of policy/procedure documents with citations, plus automated tests, evaluation metrics, and GitHub Actions CI.

## LOCAL SETUP
### 1) Create venv + install dependencies
   python -m venv .venv
   - Git Bash (Windows):
   source .venv/Scripts/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt

### 2) Configure environment variables
   cp .env.example .env
   Then edit .env and set your API key(s). Never commit .env.
   
   - Edit .env and set at minimum:
	OPENAI_API_KEY=your_key_here

### 3) Build the index (local vector DB)
	This step loads documents from data/raw/, cleans them, chunks them, embeds them, and stores them in a persistent local ChromaDB directory.

	Run:
		python -m src.ingest

	Expected output includes counts similar to:
	- Docs: 11
	- Chunks: 448
	- Upserted: 448
	- Stored count: 448 (may vary depending on Chroma version, but should be > 0)

### 4) Run the web app
	Run:
	  python -m src.app

	Open in a browser:
	  http://127.0.0.1:5000/

	Health check endpoint:
	  http://127.0.0.1:5000/health

### 5) Run tests
	pytest -q
	   
	Expected:
		- All tests pass
		- Tests do not call external APIs because the /chat logic is stubbed during tests

### 7) Run evaluation
	Run:
	  python -m eval.run_eval

	This generates:
	- eval/results.jsonl

	And prints latency summary statistics (p50/p95).

### 8) Manual scoring workflow (if scoring artifacts are included)
	Generate the scoring template:
	  python -m eval.make_score_sheet

	After filling in grounded and citation_accurate (1/0) for each row, summarize:
	  python -m eval.summarize_scores

	This writes:
	- eval/score_report.md

	Notes on persistence
	- The vector database is stored locally at vectorstore/chroma_db/.
	- To rebuild from scratch, delete vectorstore/chroma_db/ and re-run:
	  python -m src.ingest

## REPO STRUCTURE
	- data/raw/        — source documents
	- data/processed/  — cleaned/chunked artifacts (ignored by git)
	- vectorstore/     — local vector DB persistence (ignored by git)
	- src/             — application code
	- tests/           — pytest tests
	- eval/            — evaluation questions + scripts