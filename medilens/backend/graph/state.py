# backend/graph/state.py

from typing import TypedDict, List, Optional

from core.models import RetrievedChunk


class GraphState(TypedDict, total=False):
    """
    Shared state passed through the multi-agent graph.

    Each agent reads from and writes to this state.
    """

    # =====================
    # INPUT
    # =====================
    query: str

    # =====================
    # RETRIEVER OUTPUT
    # =====================
    retrieved_chunks: List[RetrievedChunk]

    # =====================
    # GENERATOR OUTPUT
    # =====================
    generated_answer: str

    # =====================
    # FACT CHECKER OUTPUT
    # =====================
    checked_answer: str
    is_verified: bool

    # =====================
    # CITATION OUTPUT
    # =====================
    citations: List[str]

    # =====================
    # SUMMARISER OUTPUT
    # =====================
    summary: Optional[str]

    # =====================
    # FINAL OUTPUT
    # =====================
    final_answer: str
