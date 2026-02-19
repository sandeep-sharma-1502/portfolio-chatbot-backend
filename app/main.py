import os
import warnings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Clean HuggingFace logs (optional but recommended)
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
warnings.filterwarnings("ignore", category=UserWarning)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router


app = FastAPI(
    title="Resume RAG Chatbot",
    version="1.0.0"
)

# Enable CORS (important if frontend is separate)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)


@app.get("/")
def health():
    return {"status": "running"}
