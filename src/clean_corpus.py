from __future__ import annotations

from src.load_corpus import load_corpus
from src.cleaning import clean_text


def main() -> None:
    docs = load_corpus()
    print(f"Loaded {len(docs)} documents for cleaning preview.\n")

    # Show before/after for first 3 docs (deterministic)
    for d in docs[:3]:
        before_len = len(d.text)
        after = clean_text(d.text)
        after_len = len(after)

        print(f"=== {d.doc_id} ===")
        print(f"Title: {d.title}")
        print(f"Before chars: {before_len}")
        print(f"After chars:  {after_len}")
        print("Preview (first 400 chars after cleaning):")
        print(after[:400].replace("\n", "\\n"))
        print()

    # Sanity: ensure cleaning doesn't blank everything
    cleaned_all = [clean_text(d.text) for d in docs]
    zero = [docs[i].doc_id for i, t in enumerate(cleaned_all) if len(t.strip()) == 0]
    if zero:
        raise SystemExit(f"Cleaning produced empty text for: {zero}")

    print("Cleaning sanity check passed (no empty docs).")

if __name__ == "__main__":
    main()