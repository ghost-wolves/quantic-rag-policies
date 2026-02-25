from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    # Reproducibility
    seed: int = 42

    # Chunking (defaults; we will tune later)
    chunk_size: int = 800
    chunk_overlap: int = 150

    # Retrieval
    top_k: int = 5

settings = Settings()
