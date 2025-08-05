# Guido API - Documentação da Arquitetura

## Visão Geral

A Guido API é uma API de integração moderna construída com FastAPI e Python, projetada para facilitar a integração com serviços externos e fornecer uma base sólida para desenvolvimento de APIs.

## Princípios Arquiteturais

### 1. Separação de Responsabilidades
- **Models**: Definem a estrutura do banco de dados (SQLAlchemy)
- **Schemas**: Definem a validação e serialização de dados (Pydantic)
- **Services**: Contêm a lógica de negócio e integrações
- **API**: Contém apenas a lógica de roteamento e validação de entrada
- **Utils**: Funções auxiliares reutilizáveis

### 2. Configuração Centralizada
- Todas as configurações são carregadas do arquivo `app/config.py`
- Variáveis de ambiente são usadas para configurações sensíveis
- Suporte a diferentes ambientes (desenvolvimento, produção)

### 3. Injeção de Dependência
- Uso de dependency injection do FastAPI
- Facilita testes e manutenção
- Reduz acoplamento entre componentes

### 4. Tratamento de Erros
- Exceções HTTP padronizadas
- Logs estruturados
- Respostas de erro consistentes

## Estrutura do Projeto

```
guido-api/
├── app/                          # Pacote principal da aplicação
│   ├── __init__.py
│   ├── main.py                   # Ponto de entrada da aplicação
│   ├── config.py                 # Configurações centralizadas
│   ├── database.py               # Configuração do banco de dados
│   ├── models/                   # Modelos SQLAlchemy
│   │   ├── __init__.py
│   │   └── user.py              # Exemplo de modelo
│   ├── schemas/                  # Schemas Pydantic
│   │   ├── __init__.py
│   │   ├── user.py              # Schemas de usuário
│   │   ├── health.py            # Schemas de health check
│   │   └── integration.py       # Schemas de integração
│   ├── api/                     # Rotas da API
│   │   └── v1/                  # Versão 1 da API
│   │       ├── __init__.py
│   │       ├── api.py           # Roteador principal v1
│   │       └── endpoints/       # Endpoints específicos
│   │           ├── __init__.py
│   │           ├── health.py    # Health check
│   │           └── integration.py # Integração com APIs externas
│   ├── services/                # Lógica de negócio
│   │   └── __init__.py
│   └── utils/                   # Utilitários
│       └── __init__.py
├── tests/                       # Testes
│   ├── __init__.py
│   └── test_health.py          # Testes de exemplo
├── requirements.txt             # Dependências
├── .env.example                # Exemplo de variáveis de ambiente
├── setup.py                    # Script de setup
└── README.md                   # Documentação principal
```

## Tecnologias Utilizadas

### Core
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **SQLAlchemy**: ORM para banco de dados
- **Alembic**: Migrações de banco de dados

### Integração e Cache
- **httpx**: Cliente HTTP assíncrono para APIs externas
- **Redis**: Cache e filas de mensagens
- **Celery**: Processamento assíncrono

### Desenvolvimento e Testes
- **pytest**: Framework de testes
- **black**: Formatação de código
- **isort**: Organização de imports
- **flake8**: Linting

## Padrões de Desenvolvimento

### 1. Nomenclatura
- Arquivos e diretórios em snake_case
- Classes em PascalCase
- Constantes em UPPER_CASE
- Variáveis e funções em snake_case

### 2. Documentação
- Docstrings em português para funções públicas
- Comentários explicativos para lógica complexa
- README.md atualizado

### 3. Testes
- Testes unitários para funções críticas
- Testes de integração para endpoints
- Cobertura de código

### 4. Segurança
- Validação de entrada com Pydantic
- Sanitização de dados
- Headers de segurança
- Rate limiting (a implementar)

## Fluxo de Dados

1. **Requisição HTTP** → FastAPI Router
2. **Validação** → Pydantic Schema
3. **Processamento** → Service Layer
4. **Persistência** → Database (se necessário)
5. **Resposta** → Pydantic Schema → JSON

## Configuração de Ambiente

### Desenvolvimento
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env

# Executar API
uvicorn app.main:app --reload
```

### Produção
```bash
# Usar gunicorn ou uvicorn com workers
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Monitoramento e Logs

- Logs estruturados em JSON
- Métricas de performance
- Health checks
- Monitoramento de APIs externas

## Próximos Passos

1. Implementar autenticação JWT
2. Adicionar rate limiting
3. Implementar cache com Redis
4. Configurar Celery para tarefas assíncronas
5. Adicionar mais testes
6. Configurar CI/CD
7. Implementar monitoramento

## Contribuição

1. Seguir os padrões estabelecidos
2. Adicionar testes para novas funcionalidades
3. Atualizar documentação
4. Usar commits semânticos
5. Criar pull requests com descrição clara 