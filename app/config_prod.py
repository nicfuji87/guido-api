# AI dev note: Configurações de produção para Render
import os
from app.config import Settings


class ProductionSettings(Settings):
    """AI dev note: Configurações específicas para produção"""
    
    # Override para produção
    debug: bool = False
    
    # Render fornece a porta via variável de ambiente
    port: int = int(os.getenv("PORT", 8000))
    
    # Configurações de segurança para produção
    secret_key: str = os.getenv("SECRET_KEY", "change-this-in-production")
    
    # Supabase - deve ser configurado no Render
    supabase_url: str = os.getenv("SUPABASE_URL", "")
    supabase_key: str = os.getenv("SUPABASE_KEY", "")
    supabase_service_role_key: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "")
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instância global das configurações de produção
prod_settings = ProductionSettings() 