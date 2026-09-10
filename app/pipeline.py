"""
Connects the retriever and the generator into one flow: question in,
grounded answer (+ the chunks it was grounded in) out.

This is the single function main.py calls on every turn of the chat loop.
"""
from typing import List, Optional, TypedDict

from app.config import TOP_K
from app.generator import generate_answer
from app.retriever import RetrievedChunk, retrieve


class PipelineResult(TypedDict):
    answer: str
    chunks: List[RetrievedChunk]


def answer_question(question: str, top_k: Optional[int] = None) -> PipelineResult:
    """Retrieve the most relevant chunks for `question`, then generate a
    grounded answer from them. Returns both, so the caller can show the
    user where the answer came from."""
    chunks = retrieve(question, top_k=top_k or TOP_K)
    answer = generate_answer(question, chunks)
    return {"answer": answer, "chunks": chunks}
