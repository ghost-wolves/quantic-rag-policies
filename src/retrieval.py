from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any

from src.config import settings
from src.vectorstore import query as chroma_query


@dataclass(frozen=True)
class RetrievedChunk:
    chunk_id: str
    doc_id: str
    title: str
    source_path: str
    start_char: int
    end_char: int
    text: str
    distance: float


def retrieve(query_text: str, top_k: int | None = None) -> List[RetrievedChunk]:
    k = top_k if top_k is not None else settings.top_k
    res = chroma_query(query_text, top_k=k)

    ids = res["ids"][0]
    docs = res["documents"][0]
    metas = res["metadatas"][0]
    dists = res["distances"][0]

    out: List[RetrievedChunk] = []
    for cid, txt, m, dist in zip(ids, docs, metas, dists):
        out.append(
            RetrievedChunk(
                chunk_id=cid,
                doc_id=m.get("doc_id", ""),
                title=m.get("title", ""),
                source_path=m.get("source_path", ""),
                start_char=int(m.get("start_char", 0)),
                end_char=int(m.get("end_char", 0)),
                text=txt,
                distance=float(dist),
            )
        )
    return out


def main() -> None:
    q = "What does the policy say about personal devices?"
    hits = retrieve(q, top_k=5)
    print(f"Query: {q}")
    print(f"Hits: {len(hits)}")
    for h in hits[:3]:
        print(f"- {h.chunk_id} | {h.doc_id} | dist={h.distance:.4f} | {h.title!r}")

if __name__ == "__main__":
    main()
