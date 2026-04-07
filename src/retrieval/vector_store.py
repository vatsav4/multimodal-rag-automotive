from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

INDEX_DIR = "faiss_index"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = None


def create_vector_store(chunks):
    """Create an in-memory FAISS vector store from chunks and persist it to disk."""
    global vector_db

    texts = [c["content"] for c in chunks]
    metadatas = [
        {
            "type": c["type"],
            "page": c["page"]
        }
        for c in chunks
    ]

    vector_db = FAISS.from_texts(texts, embedding_model, metadatas=metadatas)

    # persist to disk so other processes or later requests can load it
    try:
        os.makedirs(INDEX_DIR, exist_ok=True)
        vector_db.save_local(INDEX_DIR)
        print(f"Vector DB created with {len(texts)} chunks and saved to {INDEX_DIR}")
    except Exception as e:
        print("Warning: failed to save FAISS index:", e)

    return vector_db


def load_vector_store():
    """Load persisted FAISS index from disk into memory if available."""
    global vector_db

    if vector_db is not None:
        return vector_db

    if os.path.isdir(INDEX_DIR):
        try:
            vector_db = FAISS.load_local(INDEX_DIR, embedding_model)
            print(f"Loaded vector DB from {INDEX_DIR}")
            return vector_db
        except Exception as e:
            print("Warning: failed to load FAISS index:", e)

    return None


def get_vector_db():
    return vector_db if vector_db is not None else load_vector_store()