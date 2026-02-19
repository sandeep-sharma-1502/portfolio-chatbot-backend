import os
from groq import Groq

from app.services.vector_store import get_vector_store

_client: Groq | None = None


def get_groq_client() -> Groq:
    global _client

    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY not found in environment")

        _client = Groq(api_key=api_key)

    return _client


def ask_resume(question: str) -> str:
    if not question.strip():
        return "Please ask a valid question."

    vector_store = get_vector_store()
    docs = vector_store.similarity_search(question, k=4)

    if not docs:
        return "This information is not available in the resume."

    context = "\n\n".join(doc.page_content for doc in docs)

    client = get_groq_client()

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": (
                "You are Sandeep Sharma’s personal portfolio assistant. "
                "You answer questions only about Sandeep Sharma — his skills, experience, projects, "
                "education, and professional background. "
                "If a question is unrelated to Sandeep Sharma, politely guide the user back to "
                "asking about his professional profile. "
                "Do NOT mention resumes, documents, or sources."
            )
        },
        {
            "role": "user",
            "content": f"""
            Context:
            {context}

            User Question:
            {question}
            """
                    }
                ],
                temperature=0.2
            )
    return response.choices[0].message.content.strip()
