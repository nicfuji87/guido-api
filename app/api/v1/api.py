# AI dev note: Roteador principal da API v1
# Incluir todos os endpoints da versão 1 da API

from fastapi import APIRouter
from app.api.v1.endpoints import health, integration, guido

api_router = APIRouter()

# AI dev note: Incluir todos os roteadores de endpoints
api_router.include_router(health.router, tags=["health"])
api_router.include_router(integration.router, prefix="/integration", tags=["integration"])
api_router.include_router(guido.router, prefix="/guido", tags=["guido"]) 