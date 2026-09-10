# Models
EMBED_MODEL = "nomic-embed-text"
GEN_MODEL = "qwen3:8b"

# Storage
DATA_DIR = "data"   #where source document live
CHROMA_DB_DIR = "chroma_db" # where the vector index is persisted
COLLECTION_NAME = "documents"

#Chunking
CHUNK_SIZE = 800    # characters per chunk (not token -- good for baseline)
CHUNK_OVERLAP = 120 # characters shared btw consecutive chunks

# Retrieval
TOP_K = 4   #how many chunks to pull back per question

# Generation
SYSTEM_PROMPT = (
    "You are a helpful assistant that answers questions using ONLY the "
    "context provided below. If the answer is not contained in the context, "
    "say \"I don't have enough information in the documents to answer that.\" "
    "Do not use outside knowledge. Cite the source file name(s) you used."
)