from core.llm_client import llm_client


def chat(medicine: str, question: str) -> str:
    prompt = f"""
You are a medical assistant.

Medicine: {medicine}
Question: {question}

Answer clearly and briefly.
"""
    return llm_client.generate(prompt)
