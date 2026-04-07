from fastapi import APIRouter, UploadFile
from src.ingestion.parser import parse_pdf
from src.retrieval.vector_store import create_vector_store
from src.retrieval.retriever import retrieve_docs
from src.models.llm import generate_answer

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "running"}


@router.post("/ingest")
async def ingest(file: UploadFile):
    result = parse_pdf(file)

    create_vector_store(result["data"])

    return {
        "message": "Ingestion successful",
        "total_chunks": result["total_chunks"],
        "image_chunks": result["images"]
    }

@router.post("/query")
def query(question: str):
    docs = retrieve_docs(question)

    if not docs:
        return {"answer": "No data available. Please ingest documents first."}

    context = "\n\n".join([doc.page_content for doc in docs])

    answer = generate_answer(context, question)

    sources = [
        {
            "page": doc.metadata.get("page"),
            "type": doc.metadata.get("type")
        }
        for doc in docs
    ]

    return {
        "question": question,
        "answer": answer,
        "sources": sources
    }