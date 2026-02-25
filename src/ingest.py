from __future__ import annotations

from src.load_corpus import load_corpus
from src.cleaning import clean_text
from src.chunking import chunk_text
from src.vectorstore import upsert_chunks, get_collection


def main() -> None:
    docs = load_corpus()

    source_path_by_doc_id = {d.doc_id: d.source_path for d in docs}

    all_chunks = []
    for d in docs:
        cleaned = clean_text(d.text)
        chunks = chunk_text(d.doc_id, d.title, cleaned)
        all_chunks.extend(chunks)

    print(f"Docs: {len(docs)}")
    print(f"Chunks: {len(all_chunks)}")

    count = upsert_chunks(all_chunks, source_path_by_doc_id)
    col = get_collection()
    # Chroma doesn't always expose an exact count in all modes, but usually does.
    try:
        stored = col.count()
    except Exception:
        stored = None

    print(f"Upserted: {count}")
    print(f"Stored count: {stored}")


if __name__ == "__main__":
    main()