# AI dev note: Schema para health check
# Schema simples para resposta de health check

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """AI dev note: Schema para resposta de health check"""
    status: str
    message: str
    version: str 