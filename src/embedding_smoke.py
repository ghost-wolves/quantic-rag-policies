from __future__ import annotations

from src.load_corpus import load_corpus
from src.cleaning import clean_text
from src.chunking import chunk_text
from src.embeddings import embed_texts

def main() -> None:
    docs = load_corpus()
    cleaned = clean_text(docs[0].text)
    chunks = chunk_text(docs[0].doc_id, docs[0].title, cleaned)
    one = chunks[0].text

    vecs = embed_texts([one])
    v = vecs[0]
    print("embedding_len:", len(v))
    print("first_5:", [round(x, 6) for x in v[:5]])

if __name__ == "__main__":
    main()