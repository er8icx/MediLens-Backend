
from fastapi import FastAPI
from backend.core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

@app.get("/")
def read_root():
    return {"message": f"Welcome to {settings.APP_NAME}"}
