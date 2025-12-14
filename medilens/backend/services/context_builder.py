# backend/services/context_builder.py

from typing import List
from core.models import RetrievedChunk


def build_rag_context(
    chunks: List[RetrievedChunk],
    max_chars: int = 3000
) -> str:
    """
    Build a single context string from retrieved chunks for RAG.

    - Concatenate relevant chunks in order.
    - Stop when max_chars is reached.
    - Return plain text that will be given to the LLM.
    """
    context_parts: List[str] = []
    total = 0

    for chunk in chunks:
        text = chunk.text.strip()
        if not text:
            continue

        length = len(text)
        if total + length > max_chars:
            break

        context_parts.append(text)
        total += length

    if not context_parts:
        return "No trusted context available."

    return "\n\n".join(context_parts)
