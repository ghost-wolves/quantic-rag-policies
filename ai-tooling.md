# AI Tooling

## Tools Used
- **ChatGPT**: Used for planning the implementation steps, generating code scaffolding, debugging errors, and drafting documentation content.
- **OpenAI API (Embeddings + Chat)**: Used by the application at runtime to embed policy chunks and generate answers grounded in retrieved excerpts.

## How AI Was Used
### Planning and project structure
ChatGPT was used to create a step-by-step implementation plan with testable checkpoints (git setup, ingestion, vector DB, retrieval, RAG, web app, tests, CI, and evaluation).

### Code generation and refactoring
ChatGPT was used to:
- Create initial versions of the loaders (PDF/MD/TXT/HTML), cleaning, chunking, vector store integration, retrieval wrapper, and RAG pipeline modules.
- Create a local Flask web app with `/`, `/health`, and `/chat` routes.
- Create pytest smoke tests and a GitHub Actions CI workflow.
- Create evaluation tooling (question set schema, eval runner, scoring workflow scripts).

### Debugging assistance
ChatGPT was used to diagnose and fix issues encountered during development, including:
- Python entrypoint issues (scripts that imported but did not execute).
- A corrupted `src/config.py` file causing a syntax error.
- ChromaDB query API usage (`include` parameter should not include `ids`).
- Test failures caused by serializing non-dataclass objects with `asdict()`.

### Documentation and evaluation write-ups
ChatGPT helped draft `design-and-evaluation.md` and this `ai-tooling.md`, ensuring concrete metrics (latency p50/p95) and reproducible commands were included.

## What Worked Well
- Rapid scaffolding of small, testable modules (loader → cleaner → chunker → embeddings → vector store).
- Fast iteration on bugs using stack traces and minimal patches.
- Producing evaluation tooling and documentation templates quickly.

## What Didn’t Work / Limitations
- Some policy questions could not be answered due to corpus coverage gaps (e.g., BYOD/personal device network access).
- Automated scoring heuristics can be overly optimistic; manual review is still important for groundedness and citation accuracy.
- PDF extraction quality varies, which can affect chunk coherence and citation precision.

## How I Ensured Integrity
- Secrets were kept out of version control via `.env` and `.gitignore`.
- Automated tests and CI were used to ensure core endpoints function without calling external APIs.
- Evaluation outputs and scoring artifacts are saved to files for reproducibility.
