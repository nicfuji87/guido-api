# AI dev note: Schemas para integração com APIs externas
# Schemas para requisições e respostas de integração

from typing import Dict, Any, Optional
from pydantic import BaseModel


class IntegrationRequest(BaseModel):
    """AI dev note: Schema para requisição de integração"""
    data: Dict[str, Any]
    endpoint: Optional[str] = None
    method: str = "POST"
    headers: Optional[Dict[str, str]] = None


class IntegrationResponse(BaseModel):
    """AI dev note: Schema para resposta de integração"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: str
    error: Optional[str] = None
    status_code: Optional[int] = None 