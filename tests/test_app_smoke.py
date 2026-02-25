from __future__ import annotations

import types

import pytest

import src.app as app_module


def test_app_imports():
    assert hasattr(app_module, "app")


def test_health_endpoint():
    client = app_module.app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_chat_endpoint_returns_expected_shape(monkeypatch):
    # Stub answer_question so we don't hit OpenAI during tests
    FakeCitation = types.SimpleNamespace
    FakeChunk = types.SimpleNamespace

    def fake_answer_question(question: str, top_k: int = 5):
        return types.SimpleNamespace(
            answer="Stubbed answer",
            citations=[
                FakeCitation(
                    doc_id="doc1",
                    title="Doc 1",
                    source_path="data/raw/doc1.pdf",
                    chunk_id="doc1__00000",
                    start_char=0,
                    end_char=100,
                )
            ],
            used_chunks=[
                FakeChunk(
                    chunk_id="doc1__00000",
                    doc_id="doc1",
                    title="Doc 1",
                    source_path="data/raw/doc1.pdf",
                    start_char=0,
                    end_char=100,
                    distance=0.1,
                    text="Example snippet text",
                )
            ],
        )

    monkeypatch.setattr(app_module, "answer_question", fake_answer_question)

    client = app_module.app.test_client()
    resp = client.post("/chat", json={"question": "Test?"})
    assert resp.status_code == 200

    data = resp.get_json()
    assert isinstance(data, dict)
    assert "answer" in data and isinstance(data["answer"], str)
    assert "citations" in data and isinstance(data["citations"], list)
    assert "snippets" in data and isinstance(data["snippets"], list)

    # Check one citation and snippet has expected fields
    c0 = data["citations"][0]
    for k in ["doc_id", "title", "source_path", "chunk_id", "start_char", "end_char"]:
        assert k in c0

    s0 = data["snippets"][0]
    for k in ["chunk_id", "doc_id", "title", "source_path", "start_char", "end_char", "distance", "text"]:
        assert k in s0