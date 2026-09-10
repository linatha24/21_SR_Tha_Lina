# Demo RAG: Local Retrieval-Augmented Generation System

A lightweight, privacy-focused, and 100% local Retrieval-Augmented Generation (RAG) system built with **Python**, **Ollama**, and **ChromaDB**. 

The system indexes local knowledge base documents (`.txt`, `.md`, `.pdf`), performs semantic vector search using local embeddings, and produces grounded answers with exact source citations while refusing to hallucinate when information is missing.

---

## Features

- **100% Local & Private**: No cloud API keys or external services required. All embeddings and LLM generations run locally via Ollama.
- **Multi-Format Ingestion**: Supports `.txt`, `.md`, and `.pdf` files.
- **Deterministic Chunking**: Configurable fixed-size chunking with sliding-window overlap to preserve context across boundaries.
- **Persistent Vector Store**: Uses ChromaDB to persist chunk embeddings across runs.
- **Grounded Generation & Source Citations**: Prompt-augmented generation ensures answers strictly rely on retrieved context and cite source documents.
- **Out-of-Scope Defense**: Specifically tuned to decline answering when the context does not contain sufficient information instead of hallucinating.
- **Inspection & Debugging Tools**: Includes test scripts that report chunk similarity distances to verify retrieval precision.

---

## Architecture

```
[ Documents: .txt / .md / .pdf ]
               │
               ▼
      ( Text Extraction )
               │
               ▼
     ( Fixed Chunking + Overlap )
               │
               ▼
  [ Ollama: nomic-embed-text ] ──► ( Vector Embeddings )
                                           │
                                           ▼
                               [ ChromaDB Persistent Index ]
                                           ▲
═══════════════════════════════════════════╪═══════════════════════════════════════
 ONLINE QUERY PIPELINE                     │
                                           │
  [ User Query ] ──► [ Embed Query ] ──────┴──► [ Top-K Cosine Retrieval ]
                                                         │
                                                         ▼
                                            [ Grounded Prompt Assembly ]
                                                         │
                                                         ▼
                                             [ Ollama: qwen3:8b ]
                                                         │
                                                         ▼
                                            [ Answer + Citations ]
```

---

## Tech Stack

- **Language**: Python 3.12+
- **Dependency Management**: [Poetry](https://python-poetry.org/)
- **LLM & Embeddings Provider**: [Ollama](https://ollama.com/)
  - Embedding Model: `nomic-embed-text`
  - Generation Model: `qwen3:8b`
- **Vector Database**: [ChromaDB](https://www.trychroma.com/)
- **Document Processing**: [pypdf](https://pypdf.readthedocs.io/)

---

## Project Structure

```text
Demo-RAG/
├── app/
│   ├── config.py         # System configuration (models, chunking, top-k, prompts)
│   ├── embeddings.py     # Unified embedding interface via Ollama
│   ├── generate.py       # Prompt augmentation and LLM answer generation
│   ├── ingest.py         # Document parsing, chunking, embedding, and indexing
│   ├── main.py           # Interactive CLI chat interface
│   ├── pipeline.py       # End-to-end RAG pipeline coordination
│   ├── retrieval.py      # Semantic search and top-k chunk retrieval
│   └── vector_store.py   # ChromaDB client and collection management
├── Data/                 # Knowledge base documents (.txt, .md, .pdf)
├── chroma_db/            # Persisted ChromaDB vector store
├── scripts/
│   └── test_queries.py   # Diagnostic script for query evaluation and distance logging
├── pyproject.toml        # Project dependencies and packaging settings
├── poetry.lock           # Locked dependency tree
├── Test_Log.md           # Benchmark log of test queries and responses
└── README.md             # Project documentation
```

---

## Getting Started

### 1. Prerequisites

1. **Python 3.12+**: Ensure Python is installed.
2. **Poetry**: Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```
3. **Ollama**: Download and install Ollama from [ollama.com](https://ollama.com/).

### 2. Pull Required Models

Start the Ollama service and pull the required models:

```bash
ollama pull nomic-embed-text
ollama pull qwen3:8b
```

### 3. Install Dependencies

In the project root directory, install all dependencies with Poetry:

```bash
poetry install
```

---

## Usage

### 1. Add Documents

Place your knowledge base files into the `Data/` folder. The system supports:
- Plain text (`.txt`)
- Markdown (`.md`)
- PDF files (`.pdf`)

*(Sample IT support guides are already provided in the repository).*

### 2. Build the Vector Index

Run the ingestion script to process documents, create chunks, generate embeddings, and store them in ChromaDB:

```bash
poetry run python -m app.ingest
```

Output:
```text
Indexed 20 chunks from 'data/' into Chroma at 'chroma_db/'.
```

> **Note**: Run this command whenever you add, remove, or modify files in `Data/`.

### 3. Start Interactive Chat

Run the terminal chat interface:

```bash
poetry run python -m app.main
```

Example session:
```text
Chat with your documents. Type 'exit' to quit.

You: How do I reset my forgotten PIN?

Bot: To reset your forgotten PIN, follow these steps:
1. Access the PIN Reset Tool via the IT Support menu.
2. Authenticate with your username and password.
3. Verify your identity with your security questions.
4. Set and confirm your new PIN.

(sources: 002_Resetting_a_Forgotten_PIN.txt)

You: What is the CEO's home address?

Bot: I don't have enough information in the documents to answer that.

You: exit
Goodbye!
```

### 4. Run Retrieval Diagnostics

To test retrieval quality and observe chunk similarity distances:

```bash
poetry run python -m scripts.test_queries
```

This runs pre-configured in-scope and out-of-scope questions, displaying:
- Retrieved chunk IDs and previews
- Distance scores (smaller distance = higher semantic similarity)
- Final generated answers
- Warnings for weak retrieval matches (`dist > 1.0`)

---

## Configuration

All core hyperparameters and configurations can be modified in [`app/config.py`](app/config.py):

| Parameter | Default | Description |
| :--- | :--- | :--- |
| `EMBED_MODEL` | `"nomic-embed-text"` | Ollama embedding model name |
| `GEN_MODEL` | `"qwen3:8b"` | Ollama generation LLM name |
| `DATA_DIR` | `"data"` | Path to source documents directory |
| `CHROMA_DB_DIR` | `"chroma_db"` | Path where vector store is persisted |
| `COLLECTION_NAME` | `"documents"` | ChromaDB collection identifier |
| `CHUNK_SIZE` | `800` | Number of characters per text chunk |
| `CHUNK_OVERLAP` | `120` | Character overlap between adjacent chunks |
| `TOP_K` | `4` | Number of relevant chunks retrieved per query |
| `SYSTEM_PROMPT` | *(Grounded Prompt)* | Strict instructions enforcing document-only facts and citations |

---

## How It Works

1. **Ingestion (`app/ingestion.py`)**:
   - Files are discovered in `Data/` and their plain text is extracted.
   - Text is split into fixed-size chunks of 800 characters with 120-character overlap.
   - Each chunk receives a deterministic ID (`<filename>::<chunk_index>`) and metadata containing the source file.
   - Embeddings are generated in batches via `ollama.embed()` and stored in a local ChromaDB collection.

2. **Retrieval (`app/retriever.py`)**:
   - When a user asks a question, the query is converted into an embedding using the exact same embedding model (`nomic-embed-text`).
   - ChromaDB computes vector similarity and returns the top 4 chunks with cosine distance scores.

3. **Generation (`app/generator.py`)**:
   - Retrieved chunks are assembled into a structured prompt with source indicators.
   - The LLM (`qwen3:8b`) receives the prompt with a system rule requiring it to cite sources and refuse questions not answerable from the text.

---

