# AI dev note: Endpoint de health check
# Endpoint básico para verificar se a API está funcionando

from fastapi import APIRouter
from app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """AI dev note: Endpoint para verificar a saúde da API"""
    return HealthResponse(
        status="healthy",
        message="Guido API is running",
        version="1.0.0"
    ) 