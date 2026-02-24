from __future__ import annotations

from pathlib import Path

from src.doc_registry import build_registry, validate_registry
from src.loaders import LoadedDocument, load_by_extension, guess_title_from_text


def load_corpus() -> list[LoadedDocument]:
    registry = build_registry()
    validate_registry(registry)

    loaded: list[LoadedDocument] = []
    for meta in registry:
        p = Path(meta.source_path)
        text = load_by_extension(p)

        # improve title if we can extract one, else keep registry title
        title_guess = guess_title_from_text(text)
        title = title_guess if title_guess else meta.title

        loaded.append(
            LoadedDocument(
                doc_id=meta.doc_id,
                title=title,
                source_path=meta.source_path,
                text=text,
            )
        )
    return loaded


def main() -> None:
    docs = load_corpus()
    print(f"Loaded {len(docs)} documents.")
    for d in docs:
        print(f"- {d.doc_id}: {len(d.text)} chars | title={d.title!r}")


if __name__ == "__main__":
    main()
