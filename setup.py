#!/usr/bin/env python3
"""
AI dev note: Script de setup para a Guido API
Este script facilita a configuração inicial do projeto
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """AI dev note: Executar comando e mostrar descrição"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} concluído com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao {description.lower()}: {e}")
        print(f"Saída de erro: {e.stderr}")
        return False


def create_env_file():
    """AI dev note: Criar arquivo .env se não existir"""
    env_file = Path(".env")
    if not env_file.exists():
        print("\n📝 Criando arquivo .env...")
        try:
            with open(".env.example", "r") as example_file:
                example_content = example_file.read()
            
            with open(".env", "w") as env_file:
                env_file.write(example_content)
            
            print("✅ Arquivo .env criado com sucesso!")
            print("⚠️  Lembre-se de configurar as variáveis de ambiente no arquivo .env")
            return True
        except FileNotFoundError:
            print("❌ Arquivo .env.example não encontrado!")
            return False
    else:
        print("✅ Arquivo .env já existe!")
        return True


def main():
    """AI dev note: Função principal do setup"""
    print("🚀 Configurando Guido API...")
    
    # Verificar se Python está instalado
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ é necessário!")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    
    # Criar ambiente virtual
    if not run_command("python -m venv venv", "Criando ambiente virtual"):
        sys.exit(1)
    
    # Ativar ambiente virtual e instalar dependências
    if os.name == "nt":  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Instalando dependências"):
        sys.exit(1)
    
    # Criar arquivo .env
    if not create_env_file():
        sys.exit(1)
    
    print("\n🎉 Setup concluído com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Ative o ambiente virtual:")
    if os.name == "nt":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print("2. Configure as variáveis de ambiente no arquivo .env")
    print("3. Execute a API:")
    print("   uvicorn app.main:app --reload")
    print("4. Acesse a documentação: http://localhost:8000/docs")


if __name__ == "__main__":
    main() 