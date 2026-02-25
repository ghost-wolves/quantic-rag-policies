from __future__ import annotations

import json
import time
from pathlib import Path
from statistics import median

from src.rag import answer_question


def load_questions(path: Path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        out.append(json.loads(line))
    return out


def main() -> None:
    qpath = Path("eval/questions.jsonl")
    outpath = Path("eval/results.jsonl")

    questions = load_questions(qpath)
    outpath.write_text("", encoding="utf-8")  # truncate

    latencies = []
    refusals = 0

    with outpath.open("a", encoding="utf-8") as f:
        for q in questions:
            qid = q["id"]
            question = q["question"]

            t0 = time.time()
            result = answer_question(question, top_k=5)
            t1 = time.time()

            latency_s = t1 - t0
            latencies.append(latency_s)

            if not result.citations:
                refusals += 1

            record = {
                "id": qid,
                "question": question,
                "answer": result.answer,
                "latency_s": latency_s,
                "citations": [
                    {
                        "doc_id": c.doc_id,
                        "title": c.title,
                        "source_path": c.source_path,
                        "chunk_id": c.chunk_id,
                        "start_char": c.start_char,
                        "end_char": c.end_char,
                    }
                    for c in result.citations
                ],
                "retrieved_doc_ids": [c.doc_id for c in result.citations],
            }
            f.write(json.dumps(record) + "\n")

    lat_sorted = sorted(latencies)
    p50 = median(lat_sorted)
    p95 = lat_sorted[int(0.95 * (len(lat_sorted) - 1))]
    print(f"Ran {len(questions)} questions.")
    print(f"Refusals (no citations): {refusals}")
    print(f"Latency p50: {p50:.3f}s")
    print(f"Latency p95: {p95:.3f}s")
    print(f"Wrote: {outpath.as_posix()}")


if __name__ == "__main__":
    main()
