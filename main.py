from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Multimodal RAG for Automotive Manufacturing",
    description="AI-powered assistant for shopfloor troubleshooting",
    version="1.0"
)

app.include_router(router)