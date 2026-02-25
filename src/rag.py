from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.retrieval import retrieve, RetrievedChunk

load_dotenv()


@dataclass(frozen=True)
class Citation:
    doc_id: str
    title: str
    source_path: str
    chunk_id: str
    start_char: int
    end_char: int


@dataclass(frozen=True)
class RagResult:
    answer: str
    citations: List[Citation]
    used_chunks: List[RetrievedChunk]


SYSTEM_PROMPT = """You are a policy assistant. Answer ONLY using the provided policy excerpts.
If the excerpts do not contain the answer, say you don't have enough information in the provided policies.
Always include citations by referring to the provided [C#] labels."""
# Distance threshold: if all chunks are "far", refuse.
# Cosine distance in Chroma: smaller is more similar.

MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")


def build_context(chunks: List[RetrievedChunk]) -> str:
    blocks = []
    for i, c in enumerate(chunks, start=1):
        blocks.append(
            f"[C{i}] doc_id={c.doc_id} title={c.title} path={c.source_path} "
            f"span={c.start_char}-{c.end_char}\n{c.text}"
        )
    return "\n\n---\n\n".join(blocks)


def ask_llm(question: str, context: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in .env")
    client = OpenAI(api_key=api_key)

    user_prompt = f"""Question: {question}

Policy Excerpts:
{context}

Instructions:
- Answer using only the excerpts.
- If not answerable from excerpts, say so.
- End your answer with a line: Citations: [C#], [C#], ...
"""

    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    return resp.choices[0].message.content.strip()


def answer_question(question: str, top_k: int = 5) -> RagResult:
    chunks = retrieve(question, top_k=top_k)

    # Refuse only if nothing is retrieved. The LLM will decide if excerpts are insufficient.
    if not chunks:
        return RagResult(
            answer="I don’t have enough information in the provided policies to answer that.",
            citations=[],
            used_chunks=[],
        )

    context = build_context(chunks)
    answer = ask_llm(question, context)

    citations = [
        Citation(
            doc_id=c.doc_id,
            title=c.title,
            source_path=c.source_path,
            chunk_id=c.chunk_id,
            start_char=c.start_char,
            end_char=c.end_char,
        )
        for c in chunks
    ]

    return RagResult(answer=answer, citations=citations, used_chunks=chunks)


def main() -> None:
    q = "What do these policies say about acceptable use of personal devices?"
    result = answer_question(q, top_k=5)
    print(result.answer)
    print("\nCITATIONS:")
    for i, cit in enumerate(result.citations, start=1):
        print(f"- C{i}: {cit.doc_id} | {cit.title} | {cit.source_path} | {cit.start_char}-{cit.end_char}")

if __name__ == "__main__":
    main()