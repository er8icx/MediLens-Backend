# backend/integrations/openfda_client.py

from typing import List
import requests

from core.config import Config
from core.models import RetrievedChunk


def fetch_openfda_drug_info(drug_name: str) -> List[RetrievedChunk]:
    """
    Fetch drug label information from OpenFDA.

    Returns a list of RetrievedChunk objects.
    """

    params = {
        "search": f'openfda.generic_name:"{drug_name}"',
        "limit": Config.TOP_K_RESULTS,
    }

    try:
        response = requests.get(
            Config.OPENFDA_BASE_URL,
            params=params,
            timeout=10
        )
    except requests.RequestException:
        return []

    if response.status_code != 200:
        return []

    data = response.json()
    results = data.get("results", [])

    chunks: List[RetrievedChunk] = []

    for item in results:
        text_parts = []

        # Common OpenFDA drug label fields
        if "description" in item:
            text_parts.extend(item["description"])

        if "indications_and_usage" in item:
            text_parts.extend(item["indications_and_usage"])

        if "warnings" in item:
            text_parts.extend(item["warnings"])

        if "adverse_reactions" in item:
            text_parts.extend(item["adverse_reactions"])

        if not text_parts:
            continue

        chunks.append(
            RetrievedChunk(
                text=" ".join(text_parts),
                source="openfda",
                reference=drug_name
            )
        )

    return chunks