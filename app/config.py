# AI dev note: Configurações centrais da aplicação
# Todas as variáveis de ambiente devem ser carregadas aqui
# Não hardcode valores sensíveis - sempre use variáveis de ambiente

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database
    database_url: str = "sqlite:///./guido_api.db"
    
    # Redis
    redis_url: str = "redis://localhost:6379"
    
    # API
    api_v1_str: str = "/api/v1"
    project_name: str = "Guido API"
    version: str = "1.0.0"
    debug: bool = True
    
    # Security
    secret_key: str = "your-super-secret-key-change-this-in-production"
    access_token_expire_minutes: int = 30
    algorithm: str = "HS256"
    
    # External APIs
    external_api_base_url: Optional[str] = None
    external_api_key: Optional[str] = None
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "json"
    
    # Celery
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/0"
    
    # Supabase Configuration
    supabase_url: str = ""
    supabase_key: str = ""
    supabase_service_role_key: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instância global das configurações
settings = Settings() 