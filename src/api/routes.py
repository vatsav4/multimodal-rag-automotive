from fastapi import APIRouter, UploadFile
from src.ingestion.parser import parse_pdf
from src.retrieval.vector_store import create_vector_store

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