"""
Stage 1 of the offline pipeline: turn raw files in data/ into chunks ready
to be embedded.

Flow: load files -> split into chunks -> embed each chunk -> store in Chroma.

Run directly to (re)build the index from scratch:
    poetry run python -m app.ingestion
"""

import os
from typing import List, Tuple

import chromadb
from chromadb.config import Settings
from pypdf import PdfReader
from app.chunking import chunk_text

from app.config import (
    CHROMA_DB_DIR,
    COLLECTION_NAME,
    DATA_DIR,
)
from app.embeddings import embed_texts

# Loading
def _read_text(path:str) -> str:    #load text file return as text
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def _read_pdf(path:str) -> str: #for load pdf and define path
    reader = PdfReader(path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def load_documents(data_dir: str = DATA_DIR) -> List[Tuple[str, str]]:
    """Return a list of (filename, full_text) for every .txt/.md/.pdf file in data_dir."""
    documents = []
    for filename in sorted(os.listdir(data_dir)):
        path = os.path.join(data_dir, filename)
        if not os.path.isfile(path):
            continue
        ext = filename.lower().rsplit(".", 1)[-1]
        if ext in ("txt", "md"):
            text = _read_text(path)
        elif ext == "pdf":
            text = _read_pdf(path)
        else:
            continue    # skip anything we don't know how to read
        if text.strip():
            documents.append((filename, text))
    return documents

# ---------- Indexing ----------

_CHROMA_SETTINGS = Settings(anonymized_telemetry=False)

def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    return client.get_collection(name=COLLECTION_NAME)

def build_index(data_dir: str = DATA_DIR) -> int:
    """
    Wipe and rebuild the collection from scratch from whatever is in data_dir.
    Returns the number of chunks indexed.
    """
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass # collection didn't exist yet - that's fine
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documents = load_documents(data_dir)
    if not documents:
        raise FileNotFoundError(f"No documents found in '{data_dir}/'.")

    ids, texts, metadatas = [], [], []
    for filename, full_text in documents:
        for i, chunk in enumerate(chunk_text(full_text)):
            ids.append(f"{filename}::{i}")
            texts.append(chunk)
            metadatas.append({"source": filename, "chunk_index": i})

    embeddings = embed_texts(texts)
    collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas) #type: ignore
    return len(texts)

if __name__ == "__main__":
    count = build_index()
    print(f"Indexed {count} chunks from '{DATA_DIR}/' into Chroma at '{CHROMA_DB_DIR}/'.")

