# AI dev note: Configuração do banco de dados
# Usar SQLAlchemy para ORM e Alembic para migrações
# Suportar tanto SQLite (desenvolvimento) quanto PostgreSQL (produção)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Criar engine do banco de dados
engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.database_url else {}
)

# Criar sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()


# Dependency para injeção de dependência
def get_db():
    """AI dev note: Dependency para obter sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 