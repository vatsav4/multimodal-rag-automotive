from src.retrieval.vector_store import vector_db


def retrieve_docs(query):
    if vector_db is None:
        return []

    docs = vector_db.similarity_search(query, k=5)
    return docs