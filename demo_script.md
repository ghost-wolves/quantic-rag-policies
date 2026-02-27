# Demo Script (Local)

## 0) Prep (before recording)
- Repo is up to date on main
- .env exists (OPENAI_API_KEY set)
- Vector DB already built OR you will build it on camera
- Terminal windows ready:
  - Terminal A: run commands
  - Terminal B: curl health endpoint
- Browser ready at http://127.0.0.1:5000/

## 1) Show repo + structure (30–60s)
- Open the GitHub repo page (show commit history)
- Show key files:
  - README.md
  - design-and-evaluation.md
  - ai-tooling.md
  - deployed.md (local-only)
  - eval/questions.jsonl
  - .github/workflows/ci.yml

## 2) Build index (or show it’s already built) (1–2 min)

Option A (build on camera):
  python -m src.ingest

Call out:
- Docs count
- Chunks count
- Upserted count

Option B (if already built):
- Show vectorstore/chroma_db/ exists locally
- Optionally re-run python -m src.ingest to demonstrate idempotency

## 3) Start app (30s)
Run in Terminal A:
  python -m src.app

In Terminal B:
  curl http://127.0.0.1:5000/health

Expected: {"status":"ok"}

## 4) Demo in-corpus Q&A with citations (2–3 min)
In the browser, ask 2–3 questions that are likely answerable:

1) "What activities are prohibited under the acceptable use policies?"
2) "What consequences are described for violating acceptable use policies?"
3) "What are the phases of incident response mentioned in the documents?"

Show on screen:
- Answer text
- Citations list (doc_id/title/path/span)
- Snippets used

## 5) Demo out-of-corpus refusal (30–60s)
Ask:
  "Who won the Super Bowl in 1997?"

Show on screen:
- The assistant says it lacks enough information in the provided policies
- Citations/snippets are still displayed, but the answer refuses to claim outside-corpus facts

## 6) Run tests (30–60s)
Stop the app if needed, then run:
  pytest -q

Call out:
- Tests pass
- /chat test is stubbed (does not call external APIs)

## 7) Run evaluation + show metrics artifacts (1–2 min)
Run:
  python -m eval.run_eval

Call out:
- Results are written to eval/results.jsonl
- Latency p50/p95 printed to the terminal

Show:
- eval/score_report.md (groundedness + citation accuracy)
- design-and-evaluation.md includes the same metrics

## 8) Show CI passing (30–60s)
On GitHub:
- Open Actions tab
- Show latest CI run is green
- Mention it runs on push and PR

## 9) Wrap-up (15s)
- Restate: local-only RAG system with citations, tests+CI, evaluation + metrics, and documentation.