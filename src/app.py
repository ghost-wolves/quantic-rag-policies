from __future__ import annotations

import os
from dataclasses import asdict
from flask import Flask, request, jsonify, render_template_string
from dotenv import load_dotenv

from src.rag import answer_question

load_dotenv()

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <title>Local Policy RAG</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 24px; max-width: 900px; }
      textarea { width: 100%; height: 90px; }
      button { padding: 10px 14px; margin-top: 8px; }
      .answer { margin-top: 18px; padding: 12px; border: 1px solid #ddd; border-radius: 8px; }
      .meta { margin-top: 10px; font-size: 0.9em; color: #333; }
      .chunk { margin-top: 10px; padding: 10px; background: #f7f7f7; border-radius: 8px; white-space: pre-wrap; }
      code { background: #f1f1f1; padding: 2px 4px; border-radius: 4px; }
    </style>
  </head>
  <body>
    <h1>Local Policy RAG</h1>
    <p>Ask questions about the policies in <code>data/raw/</code>. Answers include citations.</p>

    <textarea id="q" placeholder="Type your question..."></textarea><br/>
    <button onclick="send()">Ask</button>

    <div id="out"></div>

    <script>
      async function send() {
        const q = document.getElementById("q").value.trim();
        if (!q) return;

        const out = document.getElementById("out");
        out.innerHTML = "<p>Thinking...</p>";

        const res = await fetch("/chat", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({question: q})
        });

        const data = await res.json();
        let html = "";
        html += `<div class="answer"><h3>Answer</h3><div>${data.answer.replaceAll("\\n","<br/>")}</div></div>`;

        html += `<div class="meta"><h3>Citations</h3><ul>`;
        for (const c of data.citations) {
          html += `<li><b>${c.title}</b> (<code>${c.doc_id}</code>) — ${c.source_path} [${c.start_char}-${c.end_char}]</li>`;
        }
        html += `</ul></div>`;

        html += `<div class="meta"><h3>Snippets used</h3>`;
        for (const s of data.snippets) {
          html += `<div class="chunk"><b>${s.chunk_id}</b> — <code>${s.doc_id}</code><br/>${escapeHtml(s.text)}</div>`;
        }
        html += `</div>`;

        out.innerHTML = html;
      }

      function escapeHtml(str) {
        return str
          .replaceAll("&","&amp;")
          .replaceAll("<","&lt;")
          .replaceAll(">","&gt;")
          .replaceAll('"',"&quot;")
          .replaceAll("'","&#039;")
          .replaceAll("\\n","<br/>");
      }
    </script>
  </body>
</html>
"""

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/")
def index():
    return render_template_string(INDEX_HTML)

@app.post("/chat")
def chat():
    payload = request.get_json(force=True) or {}
    question = (payload.get("question") or "").strip()
    if not question:
        return jsonify({"error": "question is required"}), 400

    result = answer_question(question, top_k=5)

    citations = [asdict(c) for c in result.citations]
    snippets = [
        {
            "chunk_id": c.chunk_id,
            "doc_id": c.doc_id,
            "title": c.title,
            "source_path": c.source_path,
            "start_char": c.start_char,
            "end_char": c.end_char,
            "distance": c.distance,
            "text": c.text[:800],  # cap for UI
        }
        for c in result.used_chunks
    ]

    return jsonify(
        {
            "answer": result.answer,
            "citations": citations,
            "snippets": snippets,
        }
    )

def main():
    port = int(os.getenv("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=True)

if __name__ == "__main__":
    main()
