from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


RAW_DIR = Path("data/raw")
IGNORE_NAMES = {".gitkeep"}


@dataclass(frozen=True)
class DocumentMeta:
    doc_id: str
    title: str
    source_path: str


def _slug_from_filename(path: Path) -> str:
    # doc_id = filename without extension, normalized
    stem = path.stem.strip()
    stem = re.sub(r"\s+", "_", stem)
    stem = re.sub(r"[^A-Za-z0-9_\-]+", "", stem)
    return stem


def _fallback_title(path: Path) -> str:
    return path.stem.replace("_", " ").strip()


def build_registry() -> list[DocumentMeta]:
    files = sorted(
        [p for p in RAW_DIR.rglob("*") if p.is_file() and p.name not in IGNORE_NAMES]
    )
    registry: list[DocumentMeta] = []
    for p in files:
        doc_id = _slug_from_filename(p)
        title = _fallback_title(p)
        registry.append(
            DocumentMeta(
                doc_id=doc_id,
                title=title,
                source_path=p.as_posix(),
            )
        )
    return registry


def validate_registry(registry: list[DocumentMeta]) -> None:
    ids = [d.doc_id for d in registry]
    dupes = sorted({x for x in ids if ids.count(x) > 1})
    if dupes:
        raise SystemExit(f"Duplicate doc_id(s) found: {dupes}")

    if not registry:
        raise SystemExit("No documents found in data/raw/ (excluding .gitkeep).")


def main() -> None:
    registry = build_registry()
    validate_registry(registry)

    print(f"Documents found: {len(registry)}")
    for d in registry:
        print(f"- doc_id={d.doc_id} | title={d.title} | path={d.source_path}")


if __name__ == "__main__":
    main()