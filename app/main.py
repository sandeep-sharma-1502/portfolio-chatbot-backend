import os
import threading
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your custom modules
from app.api.chat import router as chat_router
from app.services.vector_store import _build_vector_store

load_dotenv()

# Disable HF progress bars to keep logs clean on Render
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown logic. 
    The code before 'yield' runs on startup.
    """
    # Start the vector store build in a background thread
    # to avoid blocking the main event loop.
    thread = threading.Thread(target=_build_vector_store, daemon=True)
    thread.start()
    
    yield
    # Code after 'yield' runs on shutdown (if needed)

app = FastAPI(
    title="Portfolio AI Chatbot",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routes
app.include_router(chat_router)

@app.get("/")
def health():
    """
    Health check endpoint for Render's zero-downtime deploys.
    """
    return {"status": "running", "environment": os.getenv("NODE_ENV", "production")}

if __name__ == "__main__":
    import uvicorn
    # Render provides the PORT environment variable. Default to 10000.
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)