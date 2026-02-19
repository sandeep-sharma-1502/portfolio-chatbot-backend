from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag_chain import ask_resume


router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    reply = ask_resume(request.message)
    return {"reply": reply}
