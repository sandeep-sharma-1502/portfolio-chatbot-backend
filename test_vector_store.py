from app.services.vector_store import get_vector_store


def main():
    store = get_vector_store()
    docs = store.similarity_search("What skills does Sandeep have?")

    if docs:
        print("Top Result:\n")
        print(docs[0].page_content)
    else:
        print("No results found.")


if __name__ == "__main__":
    main()
