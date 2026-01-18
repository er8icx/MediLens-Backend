import requests

class LLMClient:
    def __init__(self, model="qwen2.5:0.5b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }

        res = requests.post(self.url, json=payload, timeout=120)
        res.raise_for_status()
        return res.json()["response"].strip()

    def summarize(self, medicine: str) -> str:
        prompt = f"""
        Give a short, clear medical summary of {medicine}.
        Include:
        - What it is
        - Common uses
        - Safety notes
        Keep it concise.
        """
        return self.generate(prompt)


# IMPORTANT: export instance
llm_client = LLMClient()
