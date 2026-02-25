from __future__ import annotations

import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

# Default embedding model (can be changed later if needed)
EMBED_MODEL = os.getenv("EMBED_MODEL", "text-embedding-3-small")


def embed_texts(texts: List[str]) -> List[List[float]]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set. Put it in .env (not committed).")

    # Lazy import so tests that don't need embeddings can still run
    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]