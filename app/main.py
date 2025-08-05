# AI dev note: Ponto de entrada principal da aplicação
# Configurar FastAPI com todas as rotas e middlewares necessários

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.config import settings
from app.database import engine
from app.models import user  # Importar modelos para criar tabelas

# AI dev note: Criar tabelas no banco de dados
user.Base.metadata.create_all(bind=engine)

# AI dev note: Configurar aplicação FastAPI
app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    openapi_url=f"{settings.api_v1_str}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

# AI dev note: Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # AI dev note: Em produção, especificar origens específicas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AI dev note: Incluir rotas da API
app.include_router(api_router, prefix=settings.api_v1_str)


@app.get("/")
async def root():
    """AI dev note: Endpoint raiz da aplicação"""
    return {
        "message": "Bem-vindo à Guido API",
        "version": settings.version,
        "docs": "/docs",
        "health": f"{settings.api_v1_str}/health"
    }


@app.get("/info")
async def info():
    """AI dev note: Informações da aplicação"""
    return {
        "name": settings.project_name,
        "version": settings.version,
        "debug": settings.debug,
        "api_version": settings.api_v1_str
    } 