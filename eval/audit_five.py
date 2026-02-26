from __future__ import annotations

import json
import re
from pathlib import Path
from collections import Counter

# The 5 "high risk" IDs to audit
AUDIT_IDS = ["q08", "q10", "q13", "q17", "q15"]

STOPWORDS = set("""
a an and are as at be by for from has have he her hers him his i if in into is it its itself just me my no not of on or our ours
she so than that the their theirs them then there these they this those to too under up was we were what when where which who will with you your
""".split())

def tokenize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    toks = [t for t in text.split() if t and t not in STOPWORDS and not t.isdigit()]
    return toks

def overlap_ratio(answer: str, evidence: str) -> float:
    a = set(tokenize(answer))
    if not a:
        return 0.0
    e = set(tokenize(evidence))
    return len(a & e) / len(a)

def top_terms(text: str, n: int = 12) -> list[tuple[str, int]]:
    c = Counter(tokenize(text))
    return c.most_common(n)

def preview(text: str, limit: int = 900) -> str:
    t = text.strip().replace("\r\n", "\n").replace("\r", "\n")
    return (t[:limit] + ("..." if len(t) > limit else ""))

def main() -> None:
    bundle_path = Path("eval/scoring_bundle.jsonl")
    if not bundle_path.exists():
        raise SystemExit("Missing eval/scoring_bundle.jsonl. Generate it first.")

    rows = []
    for line in bundle_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))

    by_id = {r["id"]: r for r in rows}
    missing = [qid for qid in AUDIT_IDS if qid not in by_id]
    if missing:
        raise SystemExit(f"Missing IDs in scoring bundle: {missing}")

    out_dir = Path("eval/audits")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "audit_5_report.md"

    md = []
    md.append("# Audit Report — 5 High-Risk Evaluation Items")
    md.append("")
    md.append("This report is for manual verification of groundedness and citation accuracy.")
    md.append("It prints each question, the model answer, and the cited evidence chunks.")
    md.append("It also prints an overlap ratio as a *hint* (not a score).")
    md.append("")

    for qid in AUDIT_IDS:
        r = by_id[qid]
        question = r.get("question", "")
        answer = r.get("answer", "")
        evidence = r.get("evidence", [])
        evidence_text = "\n\n".join((e.get("text", "") or "") for e in evidence)

        ov = overlap_ratio(answer, evidence_text)

        md.append(f"## {qid}")
        md.append("")
        md.append("**Question:**")
        md.append("")
        md.append(f"> {question}")
        md.append("")
        md.append("**Answer:**")
        md.append("")
        md.append("```text")
        md.append(answer.strip())
        md.append("```")
        md.append("")
        md.append(f"**Answer↔Evidence keyword overlap ratio (hint):** `{ov:.3f}`")
        md.append("")
        md.append("**Top answer terms:** " + ", ".join([f"`{w}`({c})" for w, c in top_terms(answer)]))
        md.append("")
        md.append("### Evidence chunks")
        md.append("")

        if not evidence:
            md.append("_No evidence chunks present._")
            md.append("")
        else:
            for i, e in enumerate(evidence, start=1):
                md.append(f"#### C{i}: `{e.get('chunk_id','')}`")
                md.append(f"- doc_id: `{e.get('doc_id','')}`")
                md.append(f"- title: {e.get('title','')}")
                md.append(f"- span: {e.get('start_char','?')}-{e.get('end_char','?')}")
                md.append("")
                md.append("```text")
                md.append(preview(e.get("text", "") or "", limit=1400))
                md.append("```")
                md.append("")

        md.append("### Manual scoring checklist")
        md.append("- Groundedness (1/0): Are *all key claims* in the answer supported by the evidence above?")
        md.append("- Citation accuracy (1/0): Do the cited chunks contain the specific supporting statements?")
        md.append("")
        md.append("---")
        md.append("")

    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote: {out_path.as_posix()}")

if __name__ == "__main__":
    main()
