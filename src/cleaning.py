from __future__ import annotations

import re


def clean_text(text: str) -> str:
    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Replace non-breaking spaces
    text = text.replace("\u00A0", " ")

    # Strip trailing whitespace per line
    text = "\n".join(line.rstrip() for line in text.splitlines())

    # Collapse 3+ newlines to max 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Collapse repeated spaces/tabs inside lines (keep indentation minimal)
    text = re.sub(r"[ \t]{2,}", " ", text)

    return text.strip()