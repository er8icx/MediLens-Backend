
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MediLens"
    VERSION: str = "0.1.0"
    
    # LLM Settings
    GEMINI_API_KEY: str | None = None
    OPENAI_API_KEY: str | None = None
    
    class Config:
        env_file = ".env"

settings = Settings()
