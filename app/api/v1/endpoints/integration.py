# AI dev note: Endpoint de integração com APIs externas
# Exemplo de como integrar com serviços externos

from fastapi import APIRouter, HTTPException
from typing import Dict, Any
import httpx
from app.config import settings
from app.schemas.integration import IntegrationRequest, IntegrationResponse

router = APIRouter()


@router.post("/external-api", response_model=IntegrationResponse)
async def call_external_api(request: IntegrationRequest):
    """AI dev note: Endpoint para chamar API externa"""
    try:
        async with httpx.AsyncClient() as client:
            # AI dev note: Exemplo de chamada para API externa
            # Em produção, usar configurações do settings
            response = await client.post(
                f"{settings.external_api_base_url}/api/data",
                json=request.dict(),
                headers={
                    "Authorization": f"Bearer {settings.external_api_key}",
                    "Content-Type": "application/json"
                },
                timeout=30.0
            )
            
            if response.status_code == 200:
                return IntegrationResponse(
                    success=True,
                    data=response.json(),
                    message="Dados obtidos com sucesso"
                )
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Erro na API externa: {response.text}"
                )
                
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Erro de conexão com API externa: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno: {str(e)}"
        )


@router.get("/health-external")
async def check_external_api_health():
    """AI dev note: Verificar saúde da API externa"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.external_api_base_url}/health",
                timeout=10.0
            )
            
            return {
                "external_api_status": "healthy" if response.status_code == 200 else "unhealthy",
                "response_time": response.elapsed.total_seconds(),
                "status_code": response.status_code
            }
            
    except Exception as e:
        return {
            "external_api_status": "error",
            "error": str(e)
        } 