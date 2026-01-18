# backend/services/context_builder.py

from typing import List

from core.models import RetrievedChunk
from core.config import Config


def build_context(drug_name: str, drug_data: dict) -> str:
    """
    Builds readable context for LLM + frontend from drug data
    """

    if not drug_data:
        return f"No detailed data found for {drug_name}."

    parts = [f"Medicine name: {drug_name.capitalize()}"]

    if "purpose" in drug_data:
        parts.append(f"Purpose: {drug_data['purpose']}")

    if "indications" in drug_data:
        parts.append(f"Uses: {drug_data['indications']}")

    if "warnings" in drug_data:
        parts.append(f"Warnings: {drug_data['warnings']}")

    if "dosage" in drug_data:
        parts.append(f"Dosage: {drug_data['dosage']}")

    return "\n".join(parts)

def _trim_context(context: str) -> str:
    """
    Trim context to a safe maximum length.
    Prevents prompt overflow.
    """

    max_chars = Config.MAX_CONTEXT_CHARS

    if len(context) <= max_chars:
        return context

    return context[:max_chars] + "\n\n[Context truncated]"
