from threading import Lock
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.services.pdf_loader import load_resume_text

_vector_store = None
_embeddings = None
_is_warming = False
_lock = Lock()


def _build_vector_store():
    global _vector_store, _embeddings, _is_warming

    with _lock:
        if _vector_store is not None:
            return

        _is_warming = True

        resume_text = load_resume_text()
        if not resume_text.strip():
            raise ValueError("Resume text is empty")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=600,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""]
        )

        documents = splitter.create_documents([resume_text])

        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        _vector_store = FAISS.from_documents(documents, _embeddings)
        _is_warming = False


def get_vector_store():
    if _vector_store is None:
        raise RuntimeError("VECTOR_STORE_NOT_READY")
    return _vector_store


def is_warming_up() -> bool:
    return _is_warming
