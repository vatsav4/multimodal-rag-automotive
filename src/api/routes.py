from fastapi import APIRouter, UploadFile
from src.ingestion.parser import parse_pdf

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "running"}


@router.post("/ingest")
async def ingest(file: UploadFile):
    result = parse_pdf(file)

    return {
        "message": "Ingestion successful",
        "total_chunks": result["total_chunks"],
        "image_chunks": result["images"]
    }