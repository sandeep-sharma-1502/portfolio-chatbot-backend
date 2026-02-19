from app.services.vector_store import get_vector_store, is_warming_up

def ask_resume(question: str) -> str:
    if not question.strip():
        return "Please ask a valid question."

    if is_warming_up():
        return (
            "I'm getting ready. Please try again in a few seconds."
        )

    try:
        vector_store = get_vector_store()
    except RuntimeError:
        return "I'm still preparing my knowledge. Please try again shortly."

    docs = vector_store.similarity_search(question, k=4)

    if not docs:
        return (
            "I can help with questions about Sandeep Sharma’s "
            "professional background, skills, and experience."
        )

    # (Groq LLM code remains SAME)
