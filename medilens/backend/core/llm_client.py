
from .config import settings

class LLMClient:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        
    async def generate_text(self, prompt: str) -> str:
        # Placeholder for actual LLM call
        return "Simulated LLM response"
