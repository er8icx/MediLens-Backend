from core.llm_client import llm_client

def search_medicine(medicine: str):
    summary = llm_client.summarize(medicine)

    return {
        "medicine": medicine,
        "summary": summary,
    }
