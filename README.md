# Guido API - API de Integração

Uma API de integração moderna construída com FastAPI e Python.

## 🚀 Características

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Supabase**: Banco de dados PostgreSQL com RLS (Row Level Security)
- **Redis**: Cache e filas de mensagens
- **Celery**: Processamento assíncrono
- **Alembic**: Migrações de banco de dados
- **Pytest**: Testes automatizados
- **pgvector**: Busca vetorial para IA

## 📋 Pré-requisitos

- Python 3.8+
- Supabase (banco de dados PostgreSQL)
- Redis (opcional, para cache e filas)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd guido-api
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

5. Configure as credenciais do Supabase no arquivo `.env`

## 🚀 Executando a API

### Desenvolvimento
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Produção
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 📚 Documentação da API

Após iniciar o servidor, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testes

```bash
pytest
```

## 📁 Estrutura do Projeto

```
guido-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── config.py            # Configurações
│   ├── database.py          # Configuração do banco de dados
│   ├── models/              # Modelos SQLAlchemy
│   ├── schemas/             # Schemas Pydantic
│   ├── api/                 # Rotas da API
│   ├── services/            # Lógica de negócio
│   └── utils/               # Utilitários
├── alembic/                 # Migrações
├── tests/                   # Testes
├── requirements.txt
└── README.md
```

## 🔧 Configuração

Copie o arquivo `.env.example` para `.env` e configure as variáveis:

```env
# Supabase Configuration
SUPABASE_URL=your-supabase-project-url
SUPABASE_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

# Redis
REDIS_URL=redis://localhost:6379

# API
API_V1_STR=/api/v1
PROJECT_NAME=Guido API
VERSION=1.0.0

# Security
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. 