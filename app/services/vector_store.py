from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.services.pdf_loader import load_resume_text


_vector_store = None


def get_vector_store():
    """
    Create and cache FAISS vector store for resume embeddings.
    The vector store is initialized once and reused across requests.
    """

    global _vector_store

    if _vector_store is not None:
        return _vector_store

    resume_text = load_resume_text()
    if not resume_text.strip():
        raise ValueError("Resume text is empty")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    documents = splitter.create_documents([resume_text])

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    _vector_store = FAISS.from_documents(documents, embeddings)
    return _vector_store
