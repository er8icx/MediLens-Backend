# backend/agents/generator_agent.py

from typing import Dict, Any, List

from core.llm_client import llm_client
from core.models import RetrievedChunk
from services.context_builder import build_rag_context


async def generator_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    GENERATOR AGENT (G in RAG)

    - Takes the user query and retrieved chunks.
    - Builds a RAG-style context string.
    - Calls the LLM client with (question + context).
    - Stores the draft answer in state["draft_answer"].
    """
    query: str = state.get("query", "")
    chunks: List[RetrievedChunk] = state.get("retrieved_chunks", [])

    # Build RAG context from chunks
    context_text = build_rag_context(chunks)

    # Simple RAG prompt: you’ll later move this inside llm_client if you want
    prompt = (
        "You are MediLens, an AI assistant that provides safe, factual drug information.\n"
        "Use ONLY the information in the context below to answer the user's question.\n"
        "If the context does not contain enough information, say you are not sure and "
        "recommend consulting a healthcare professional.\n\n"
        f"Context:\n{context_text}\n\n"
        f"Question:\n{query}\n\n"
        "Answer:"
    )

    # For now, llm_client.generate_answer can just accept (question, chunks)
    # but we can overload it to accept a full prompt later.
    # Easiest: treat 'prompt' as the 'question' argument.
    answer = await llm_client.generate_answer(prompt, [])

    state["draft_answer"] = answer
    return state