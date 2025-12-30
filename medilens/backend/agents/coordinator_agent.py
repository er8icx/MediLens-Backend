# backend/agents/coordinator_agent.py

from typing import Dict, Any

from agents.retriever_agent import retriever_agent
from agents.generator_agent import generator_agent
from agents.fact_checker_agent import fact_checker_agent
from agents.citation_agent import citation_agent
from agents.summarizer import summariser_agent


async def coordinator_agent(initial_state: Dict[str, Any]) -> Dict[str, Any]:
    """
    COORDINATOR AGENT

    Orchestrates the multi-agent workflow.
    Responsible ONLY for:
    - Calling agents in correct order
    - Passing shared state between agents
    """

    state = initial_state

    # 1️⃣ Retrieve trusted information
    state = await retriever_agent(state)

    # 2️⃣ Generate draft response (RAG)
    state = await generator_agent(state)

    # 3️⃣ Fact-check generated content
    state = await fact_checker_agent(state)

    # 4️⃣ Attach citations
    state = await citation_agent(state)

    # 5️⃣ Summarise for UI (optional, non-critical)
    state = await summariser_agent(state)

    return state