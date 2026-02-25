from __future__ import annotations

from src.load_corpus import load_corpus
from src.cleaning import clean_text
from src.chunking import chunk_text


def main() -> None:
    docs = load_corpus()

    all_chunks = []
    for d in docs:
        cleaned = clean_text(d.text)
        chunks = chunk_text(d.doc_id, d.title, cleaned)
        all_chunks.extend(chunks)

    print(f"Documents: {len(docs)}")
    print(f"Total chunks: {len(all_chunks)}")
    # Show 5 sample chunks
    for c in all_chunks[:5]:
        print(f"- {c.chunk_id} | doc={c.doc_id} | chars={len(c.text)} | span={c.start_char}-{c.end_char}")

    # sanity checks
    if len(all_chunks) == 0:
        raise SystemExit("No chunks produced.")
    bad = [c.chunk_id for c in all_chunks if len(c.text.strip()) == 0]
    if bad:
        raise SystemExit(f"Empty chunks produced: {bad[:5]} ...")

    print("Chunking sanity check passed.")

if __name__ == "__main__":
    main()
