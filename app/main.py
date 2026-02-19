from dotenv import load_dotenv
load_dotenv()

import os
import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.services.vector_store import _build_vector_store

os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

app = FastAPI(
    title="Portfolio AI Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.on_event("startup")
def warmup_in_background():
    thread = threading.Thread(target=_build_vector_store, daemon=True)
    thread.start()


@app.get("/")
def health():
    return {"status": "running"}
