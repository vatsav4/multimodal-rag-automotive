from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = None


def create_vector_store(chunks):
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

    print(f"Vector DB created with {len(texts)} chunks")  # ✅ DEBUG

    return vector_db