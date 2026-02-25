from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from src.config import settings


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    doc_id: str
    title: str
    text: str
    start_char: int
    end_char: int


def chunk_text(doc_id: str, title: str, text: str) -> list[Chunk]:
    size = settings.chunk_size
    overlap = settings.chunk_overlap
    if size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0 or overlap >= size:
        raise ValueError("chunk_overlap must be >= 0 and < chunk_size")

    chunks: list[Chunk] = []
    i = 0
    n = len(text)
    idx = 0

    while i < n:
        start = i
        end = min(i + size, n)
        chunk_txt = text[start:end].strip()

        if chunk_txt:
            chunk_id = f"{doc_id}__{idx:05d}"
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    doc_id=doc_id,
                    title=title,
                    text=chunk_txt,
                    start_char=start,
                    end_char=end,
                )
            )
            idx += 1

        if end == n:
            break
        i = end - overlap

    return chunks