from src.retrieval.vector_store import get_vector_db


def retrieve_docs(query):
    vdb = get_vector_db()
    if vdb is None:
        return []

    docs = vdb.similarity_search(query, k=5)
    return docs