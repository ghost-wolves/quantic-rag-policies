from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Dict, Any

import chromadb
from chromadb.config import Settings as ChromaSettings

from src.chunking import Chunk
from src.embeddings import embed_texts

PERSIST_DIR = Path("vectorstore/chroma_db")
COLLECTION_NAME = "policy_chunks_v1"


def get_client() -> chromadb.PersistentClient:
    PERSIST_DIR.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(
        path=str(PERSIST_DIR),
        settings=ChromaSettings(anonymized_telemetry=False),
    )


def get_collection():
    client = get_client()
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )


def upsert_chunks(chunks: List[Chunk], source_path_by_doc_id: Dict[str, str]) -> int:
    col = get_collection()
    ids = [c.chunk_id for c in chunks]
    docs = [c.text for c in chunks]
    metas: List[Dict[str, Any]] = []
    for c in chunks:
        metas.append(
            {
                "doc_id": c.doc_id,
                "title": c.title,
                "source_path": source_path_by_doc_id.get(c.doc_id, ""),
                "start_char": c.start_char,
                "end_char": c.end_char,
            }
        )

    # embeddings in batches for safety
    BATCH = 64
    for i in range(0, len(chunks), BATCH):
        batch_ids = ids[i : i + BATCH]
        batch_docs = docs[i : i + BATCH]
        batch_metas = metas[i : i + BATCH]
        batch_embeds = embed_texts(batch_docs)
        col.upsert(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metas,
            embeddings=batch_embeds,
        )

    return len(chunks)


def query(query_text: str, top_k: int = 5):
    col = get_collection()
    q_emb = embed_texts([query_text])[0]
    res = col.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],
    )
    return res