"""
Owns the vector database: how we connect to it, how we save chunk vectors
into it, and how we search it later.

"""
import logging
from typing import Any, Dict, List

import chromadb
from chromadb.config import Settings

from app.config import CHROMA_DB_DIR, COLLECTION_NAME

logging.getLogger("chromadb.telemetry.product.posthog").setLevel(logging.CRITICAL)

_CHROMA_SETTINGS = Settings(anonymized_telemetry=False)


def get_collection():
    """Open (or create) the persistent Chroma collection we store chunks in."""
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    return client.get_or_create_collection(name=COLLECTION_NAME)


def reset_collection():
    """Wipe the collection so a fresh ingest run starts from nothing."""
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR, settings=_CHROMA_SETTINGS)
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass  # collection didn't exist yet -- that's fine
    return client.get_or_create_collection(name=COLLECTION_NAME)


def add_chunks(
    ids: List[str],
    texts: List[str],
    embeddings: List[List[float]],
    metadatas: List[Dict[str, Any]],
) -> None:
    """Save a batch of chunk texts + their vectors + metadata into the store."""
    collection = get_collection()
    collection.add(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadatas)  # type: ignore


def search(query_embedding: List[float], top_k: int):
    """Return the raw Chroma query result for the closest top_k chunks."""
    collection = get_collection()
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"],  # type: ignore
    )
