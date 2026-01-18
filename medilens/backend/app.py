from fastapi import FastAPI
from pydantic import BaseModel

from services.search_service import search_medicine
from services.chat_service import chat

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or "*" for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SearchRequest(BaseModel):
    medicine: str


class ChatRequest(BaseModel):
    medicine: str
    question: str


@app.post("/search")
def search(req: SearchRequest):
    print("SEARCH SERVICE HIT") 
    return search_medicine(req.medicine)


@app.post("/chat")
def chat_endpoint(req: ChatRequest):
    answer = chat(req.medicine, req.question)
    return {"answer": answer}
