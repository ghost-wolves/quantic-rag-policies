from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup
from pypdf import PdfReader
import markdown as md_lib


@dataclass(frozen=True)
class LoadedDocument:
    doc_id: str
    title: str
    source_path: str
    text: str


def load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    parts: list[str] = []
    for page in reader.pages:
        txt = page.extract_text() or ""
        parts.append(txt)
    return "\n".join(parts).strip()


def load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def load_markdown(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    html = md_lib.markdown(raw)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text("\n").strip()


def load_html(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(raw, "html.parser")
    return soup.get_text("\n").strip()


def guess_title_from_text(text: str) -> Optional[str]:
    # Heuristic: first non-empty line, capped length
    for line in (l.strip() for l in text.splitlines()):
        if line:
            return line[:120]
    return None


def load_by_extension(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return load_pdf(path)
    if ext in {".txt"}:
        return load_txt(path)
    if ext in {".md", ".markdown"}:
        return load_markdown(path)
    if ext in {".html", ".htm"}:
        return load_html(path)
    raise ValueError(f"Unsupported file type: {ext} for {path}")