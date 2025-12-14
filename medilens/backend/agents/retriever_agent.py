# backend/agents/retriever_agent.py

import json
from pathlib import Path
from typing import Dict, Any, List

from core.models import RetrievedChunk

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "drug_knowledge.json"


def _load_local_db() -> Dict[str, Dict[str, object]]:
    if not DATA_PATH.exists():
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


LOCAL_DB = _load_local_db()


async def retriever_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    RETRIEVER AGENT (R in RAG)

    - Reads the user's query.
    - Finds matching drug entries in the local JSON DB (by name).
    - Converts each match into a RetrievedChunk with rich context text.
    """
    query = state.get("query", "").lower()
    chunks: List[RetrievedChunk] = []

    for drug_name, info in LOCAL_DB.items():
        if drug_name.lower() in query:
            indications = ", ".join(info.get("indications", []))
            common_se = ", ".join(info.get("common_side_effects", []))
            warnings = " ".join(info.get("warnings", []))
            interactions = " ".join(info.get("interaction_notes", []))

            text = (
                f"Drug: {info.get('generic_name', drug_name)}\n"
                f"Class: {info.get('class', 'N/A')}\n"
                f"Brand examples: {', '.join(info.get('brand_examples', []))}\n"
                f"Indications: {indications}\n"
                f"Common side effects: {common_se}\n"
                f"Important warnings: {warnings}\n"
                f"Interaction notes: {interactions}\n"
            )

            chunks.append(
                RetrievedChunk(
                    source="local",
                    reference=f"local:{drug_name}",
                    text=text,
                )
            )

    if not chunks:
        # Fallback generic chunk
        chunks.append(
            RetrievedChunk(
                source="local",
                reference="local:generic",
                text=(
                    "No specific drug found for this query in the local database. "
                    "General reminder: Only a qualified healthcare professional can "
                    "give personalised advice about medicines."
                ),
            )
        )

    state["retrieved_chunks"] = chunks
    return state
