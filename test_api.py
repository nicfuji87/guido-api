#!/usr/bin/env python3
"""
AI dev note: Script de teste para verificar se a API está funcionando
Testa a conexão com Supabase e os endpoints básicos
"""

import asyncio
import httpx
import json
from datetime import datetime, timedelta
from uuid import uuid4


async def test_supabase_connection():
    """AI dev note: Testar conexão com Supabase"""
    print("🔍 Testando conexão com Supabase...")
    
    try:
        from app.services.supabase_service import supabase_service
        
        # Testar obtenção de planos
        planos = await supabase_service.get_planos_ativos()
        print(f"✅ Conexão com Supabase OK! Encontrados {len(planos)} planos")
        
        for plano in planos:
            print(f"   - {plano['nome_plano']}: R$ {plano['preco_mensal']}/mês")
        
        return True
    except Exception as e:
        print(f"❌ Erro na conexão com Supabase: {e}")
        return False


async def test_api_endpoints():
    """AI dev note: Testar endpoints da API"""
    print("\n🚀 Testando endpoints da API...")
    
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # Testar health check
        try:
            response = await client.get(f"{base_url}/api/v1/health")
            if response.status_code == 200:
                print("✅ Health check OK")
            else:
                print(f"❌ Health check falhou: {response.status_code}")
        except Exception as e:
            print(f"❌ Erro no health check: {e}")
        
        # Testar endpoint de planos
        try:
            response = await client.get(f"{base_url}/api/v1/guido/planos")
            if response.status_code == 200:
                planos = response.json()
                print(f"✅ Endpoint de planos OK - {len(planos)} planos encontrados")
            else:
                print(f"❌ Endpoint de planos falhou: {response.status_code}")
        except Exception as e:
            print(f"❌ Erro no endpoint de planos: {e}")
        
        # Testar criação de conta
        try:
            conta_data = {
                "nome_conta": "Teste Imobiliária",
                "tipo_conta": "IMOBILIARIA",
                "documento": "12.345.678/0001-90"
            }
            response = await client.post(
                f"{base_url}/api/v1/guido/contas",
                json=conta_data
            )
            if response.status_code == 200:
                conta = response.json()
                print(f"✅ Criação de conta OK - ID: {conta['id']}")
                return conta['id']
            else:
                print(f"❌ Criação de conta falhou: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"❌ Erro na criação de conta: {e}")
        
        return None


async def test_full_workflow():
    """AI dev note: Testar workflow completo"""
    print("\n🔄 Testando workflow completo...")
    
    base_url = "http://localhost:8000"
    
    async with httpx.AsyncClient() as client:
        # 1. Criar conta
        conta_data = {
            "nome_conta": "Imobiliária Teste",
            "tipo_conta": "IMOBILIARIA",
            "documento": "98.765.432/0001-10"
        }
        
        try:
            response = await client.post(
                f"{base_url}/api/v1/guido/contas",
                json=conta_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar conta: {response.status_code}")
                return
            
            conta = response.json()
            conta_id = conta['id']
            print(f"✅ Conta criada: {conta_id}")
            
            # 2. Criar corretor
            corretor_data = {
                "conta_id": conta_id,
                "nome": "João Silva",
                "email": "joao@imobiliaria.com",
                "funcao": "DONO",
                "hash_senha": "senha_hash_exemplo"
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/corretores",
                json=corretor_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar corretor: {response.status_code}")
                return
            
            corretor = response.json()
            corretor_id = corretor['id']
            print(f"✅ Corretor criado: {corretor_id}")
            
            # 3. Criar cliente
            cliente_data = {
                "conta_id": conta_id,
                "corretor_id": corretor_id,
                "nome": "Maria Santos",
                "telefone": "(11) 99999-9999",
                "email": "maria@email.com",
                "status_funil": "Novo"
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/clientes",
                json=cliente_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar cliente: {response.status_code}")
                return
            
            cliente = response.json()
            cliente_id = cliente['id']
            print(f"✅ Cliente criado: {cliente_id}")
            
            # 4. Criar conversa
            conversa_data = {
                "cliente_id": cliente_id,
                "plataforma": "WhatsApp",
                "status_conversa": "AGUARDANDO_CLIENTE"
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/conversas",
                json=conversa_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar conversa: {response.status_code}")
                return
            
            conversa = response.json()
            conversa_id = conversa['id']
            print(f"✅ Conversa criada: {conversa_id}")
            
            # 5. Criar mensagem
            mensagem_data = {
                "conversa_id": conversa_id,
                "remetente": "CLIENTE",
                "conteudo_texto": "Olá! Estou interessada em um apartamento de 2 quartos."
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/mensagens",
                json=mensagem_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar mensagem: {response.status_code}")
                return
            
            mensagem = response.json()
            print(f"✅ Mensagem criada: {mensagem['id']}")
            
            # 6. Criar lembrete
            lembrete_data = {
                "corretor_id": corretor_id,
                "cliente_id": cliente_id,
                "descricao": "Ligar para Maria sobre apartamento 2 quartos",
                "data_lembrete": (datetime.now() + timedelta(hours=2)).isoformat(),
                "status": "PENDENTE"
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/lembretes",
                json=lembrete_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar lembrete: {response.status_code}")
                return
            
            lembrete = response.json()
            print(f"✅ Lembrete criado: {lembrete['id']}")
            
            # 7. Criar dossiê IA
            dossie_data = {
                "cliente_id": cliente_id,
                "resumo_gerado": "Cliente interessada em apartamento de 2 quartos. Orçamento até R$ 300.000. Prefere região central.",
                "sentimento_geral": "Positivo"
            }
            
            response = await client.post(
                f"{base_url}/api/v1/guido/dossies-ia",
                json=dossie_data
            )
            if response.status_code != 200:
                print(f"❌ Erro ao criar dossiê: {response.status_code}")
                return
            
            dossie = response.json()
            print(f"✅ Dossiê IA criado: {dossie['id']}")
            
            print("\n🎉 Workflow completo testado com sucesso!")
            print(f"📊 Resumo:")
            print(f"   - Conta: {conta_id}")
            print(f"   - Corretor: {corretor_id}")
            print(f"   - Cliente: {cliente_id}")
            print(f"   - Conversa: {conversa_id}")
            print(f"   - Mensagem: {mensagem['id']}")
            print(f"   - Lembrete: {lembrete['id']}")
            print(f"   - Dossiê IA: {dossie['id']}")
            
        except Exception as e:
            print(f"❌ Erro no workflow: {e}")


async def main():
    """AI dev note: Função principal de teste"""
    print("🧪 Iniciando testes da API Guido...")
    
    # Testar conexão com Supabase
    supabase_ok = await test_supabase_connection()
    
    if not supabase_ok:
        print("❌ Falha na conexão com Supabase. Verifique as credenciais.")
        return
    
    # Testar endpoints da API
    await test_api_endpoints()
    
    # Testar workflow completo
    await test_full_workflow()
    
    print("\n✅ Todos os testes concluídos!")


if __name__ == "__main__":
    asyncio.run(main()) 