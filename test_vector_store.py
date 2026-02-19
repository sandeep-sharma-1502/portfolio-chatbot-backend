"""
Manual test file for vector store.
Run this file to verify that:
- Resume is loaded
- Embeddings are created
- FAISS similarity search works
"""

from app.services.vector_store import get_vector_store


def main():
    store = get_vector_store()

    query = "What skills does Sandeep Sharma have?"
    docs = store.similarity_search(query, k=3)

    print(f"\nQuery: {query}\n")
    print("Top Results:\n")

    for i, doc in enumerate(docs, start=1):
        print(f"--- Result {i} ---")
        print(doc.page_content)
        print()


if __name__ == "__main__":
    main()
