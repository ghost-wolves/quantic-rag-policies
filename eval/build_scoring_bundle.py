from __future__ import annotations

import json
from pathlib import Path

from src.load_corpus import load_corpus
from src.cleaning import clean_text
from src.chunking import chunk_text


def load_results(path: Path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def main() -> None:
    results_path = Path("eval/results.jsonl")
    if not results_path.exists():
        raise SystemExit("Missing eval/results.jsonl. Run: python -m eval.run_eval")

    # Rebuild cleaned text + chunks exactly like ingestion does
    docs = load_corpus()
    cleaned_by_doc = {d.doc_id: clean_text(d.text) for d in docs}

    chunks_by_id = {}
    for d in docs:
        chunks = chunk_text(d.doc_id, d.title, cleaned_by_doc[d.doc_id])
        for c in chunks:
            chunks_by_id[c.chunk_id] = {
                "chunk_id": c.chunk_id,
                "doc_id": c.doc_id,
                "title": c.title,
                "start_char": c.start_char,
                "end_char": c.end_char,
                "text": c.text,
            }

    results = load_results(results_path)
    out_path = Path("eval/scoring_bundle.jsonl")
    out_path.write_text("", encoding="utf-8")

    with out_path.open("a", encoding="utf-8") as out:
        for r in results:
            citations = r.get("citations", [])
            evidence = []
            for c in citations:
                cid = c.get("chunk_id")
                if cid and cid in chunks_by_id:
                    evidence.append(chunks_by_id[cid])
                else:
                    # fallback: at least keep metadata
                    evidence.append(
                        {
                            "chunk_id": cid,
                            "doc_id": c.get("doc_id", ""),
                            "title": c.get("title", ""),
                            "start_char": c.get("start_char", 0),
                            "end_char": c.get("end_char", 0),
                            "text": "",
                        }
                    )

            bundle_row = {
                "id": r["id"],
                "question": r["question"],
                "answer": r["answer"],
                "evidence": evidence,  # list of chunk texts
            }
            out.write(json.dumps(bundle_row) + "\n")

    print(f"Wrote: {out_path.as_posix()}")
    print("Upload eval/scoring_bundle.jsonl here and I will score everything for you.")


if __name__ == "__main__":
    main()