# Design and Evaluation

## Goal
Build a local-only RAG (Retrieval-Augmented Generation) assistant that answers questions about a small corpus of policy/procedure documents and provides citations to the source material.

## Corpus
- Documents: 11 PDF policy/procedure documents stored under `data/raw/`
- Total chunks indexed: 448

## Architecture Overview
1. **Load** documents from `data/raw/` (PDF/TXT/MD/HTML supported).
2. **Clean** extracted text (normalize whitespace, remove excess blank lines).
3. **Chunk** each document using a fixed-size sliding window with overlap.
4. **Embed** chunks using an embeddings model.
5. **Store** embeddings and metadata in a persistent local vector database (ChromaDB).
6. **Retrieve** top-k chunks for a user question.
7. **Generate** an answer using the retrieved chunks as context, requiring citations.

## Key Design Choices

### Chunking
- `chunk_size`: 800 characters
- `chunk_overlap`: 150 characters
- Provenance stored as `start_char` and `end_char` offsets.

Rationale: fixed-size chunking is deterministic and works reliably with PDF text extraction where headings may not parse cleanly.

### Retrieval
- Vector DB: ChromaDB (persistent), cosine distance
- Default retrieval depth: `top_k = 5` (web app can be adjusted)

Rationale: cosine similarity is standard for embedding retrieval; persistence allows re-running locally without re-embedding.

### Models
- Embeddings: OpenAI `text-embedding-3-small` (1536-dim vectors observed in smoke test)
- Chat model: `gpt-4o-mini` (configurable via env var)

Rationale: cost-efficient and fast for policy summarization with citations.

### Guardrails
- System prompt instructs the model to answer only from provided excerpts.
- If excerpts do not contain the answer, the model is instructed to respond that it lacks enough information.

## Evaluation

### Question Set
- 20 evaluation questions in `eval/questions.jsonl`
- Topics: acceptable use, prohibited activities, consequences, monitoring, incident response lifecycle, reporting, evidence preservation.

### System Metric: Latency
From `python -m eval.run_eval` over 20 questions:
- p50 latency: **4.041s**
- p95 latency: **8.750s**

### Answer Quality Metrics
- Results: `eval/results.jsonl`
- Manual scoring sheet: `eval/scores_template.jsonl`
- Score report: `eval/score_report.md`

## Evaluation Score Report
- Total questions: **20**
- Groundedness: 18/20 = **90.0%**
- Citation accuracy: 18/20 = **90.0%**
## Scoring Rubric
- Groundedness (1/0): Is the answer supported by the cited excerpts?
- Citation accuracy (1/0): Do the citations correspond to the specific claims made?

## Limitations / Future Improvements
- PDF extraction quality varies; heading-aware chunking could improve citation precision.
- Some questions fail due to corpus coverage gaps (e.g., BYOD/personal device network access).
- Query expansion and re-ranking could improve retrieval for ambiguous questions.
- Stronger automatic groundedness scoring could replace manual scoring in future work.

## Reproducibility
- Build index: `python -m src.ingest`
- Run app: `python -m src.app`
- Run tests: `pytest -q`
- Run evaluation: `python -m eval.run_eval`
