from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    results_path = Path("eval/results.jsonl")
    out_path = Path("eval/scores_template.jsonl")

    if not results_path.exists():
        raise SystemExit("Missing eval/results.jsonl (run eval first).")

    out_path.write_text("", encoding="utf-8")

    with results_path.open("r", encoding="utf-8") as f, out_path.open("a", encoding="utf-8") as out:
        for line in f:
            r = json.loads(line)
            score_row = {
                "id": r["id"],
                "question": r["question"],
                "answer": r["answer"],
                "grounded": None,        # set to 1 or 0
                "citation_accurate": None, # set to 1 or 0
                "notes": ""
            }
            out.write(json.dumps(score_row) + "\n")

    print(f"Wrote: {out_path.as_posix()}")
    print("Fill in grounded and citation_accurate with 1 or 0 for each row.")

if __name__ == "__main__":
    main()