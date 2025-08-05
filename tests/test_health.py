# AI dev note: Teste para endpoint de health check
# Teste básico para verificar se a API está funcionando

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """AI dev note: Teste do endpoint de health check"""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["message"] == "Guido API is running"
    assert data["version"] == "1.0.0"


def test_root_endpoint():
    """AI dev note: Teste do endpoint raiz"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "docs" in data
    assert "health" in data


def test_info_endpoint():
    """AI dev note: Teste do endpoint de informações"""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "debug" in data
    assert "api_version" in data 