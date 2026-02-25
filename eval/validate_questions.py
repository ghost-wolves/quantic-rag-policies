from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    path = Path("eval/questions.jsonl")
    if not path.exists():
        raise SystemExit("Missing eval/questions.jsonl")

    ids = []
    n = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        if "id" not in obj or "question" not in obj:
            raise SystemExit(f"Bad schema on line {n+1}: {obj}")
        ids.append(obj["id"])
        n += 1

    if not (15 <= n <= 30):
        raise SystemExit(f"Expected 15–30 questions, found {n}")

    dupes = sorted({x for x in ids if ids.count(x) > 1})
    if dupes:
        raise SystemExit(f"Duplicate ids: {dupes}")

    print(f"OK: {n} questions, unique ids.")


if __name__ == "__main__":
    main()
