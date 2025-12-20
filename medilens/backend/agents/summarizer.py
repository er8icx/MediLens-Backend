# Summarizer Agent
from typing import Dict, Any, List

from core.llm_client import llm_client
from core.models import RetrievedChunk
from services.context_builder import build_rag_context


async def summariser_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    SUMMARISER AGENT

    - Takes trusted retrieved chunks OR a verified answer
    - Produces a concise, user-friendly summary
    - Output is for UI display only (not used for fact-checking)
    """

    # Priority: summarize verified answer if available
    text_to_summarise = state.get("checked_answer")

    # Fallback: summarize retrieved context
    if not text_to_summarise:
        chunks: List[RetrievedChunk] = state.get("retrieved_chunks", [])
        text_to_summarise = build_rag_context(chunks)

    if not text_to_summarise:
        state["summary"] = "No information available to summarise."
        return state

    summary = await llm_client.summarize(
        text=text_to_summarise,
        mode="patient_friendly"
    )

    state["summary"] = summary
    return state
