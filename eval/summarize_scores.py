from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    path = Path("eval/scores_template.jsonl")
    if not path.exists():
        raise SystemExit("Missing eval/scores_template.jsonl (generate it first).")

    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))

    total = len(rows)
    if total == 0:
        raise SystemExit("No rows found.")

    missing = [r["id"] for r in rows if r["grounded"] is None or r["citation_accurate"] is None]
    if missing:
        raise SystemExit(f"Missing scores for ids: {missing[:5]} ... (fill all rows)")

    grounded_sum = sum(int(r["grounded"]) for r in rows)
    cite_sum = sum(int(r["citation_accurate"]) for r in rows)

    grounded_pct = grounded_sum / total * 100
    cite_pct = cite_sum / total * 100

    print(f"Total: {total}")
    print(f"Groundedness: {grounded_sum}/{total} = {grounded_pct:.1f}%")
    print(f"Citation accuracy: {cite_sum}/{total} = {cite_pct:.1f}%")

    report = Path("eval/score_report.md")
    report.write_text(
        "\n".join(
            [
                "# Evaluation Score Report",
                f"- Total questions: {total}",
                f"- Groundedness: {grounded_sum}/{total} = {grounded_pct:.1f}%",
                f"- Citation accuracy: {cite_sum}/{total} = {cite_pct:.1f}%",
                "",
                "## Scoring Rubric",
                "- Groundedness (1/0): Is the answer supported by the cited excerpts?",
                "- Citation accuracy (1/0): Do the citations correspond to the specific claims made?",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote: {report.as_posix()}")

if __name__ == "__main__":
    main()