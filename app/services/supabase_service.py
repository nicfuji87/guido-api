# AI dev note: Serviço para integração com Supabase
# Centraliza todas as operações com o banco de dados Supabase

import httpx
import json
from typing import Dict, Any, List, Optional
from app.config import settings


class SupabaseService:
    """AI dev note: Serviço para integração com Supabase usando httpx"""
    
    def __init__(self):
        """AI dev note: Inicializar cliente Supabase"""
        if not settings.supabase_url or not settings.supabase_key:
            raise ValueError("SUPABASE_URL e SUPABASE_KEY são obrigatórios")
        
        self.base_url = settings.supabase_url
        self.api_key = settings.supabase_key
        self.headers = {
            "apikey": self.api_key,
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
    
    async def _make_request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """AI dev note: Fazer requisição para a API do Supabase"""
        url = f"{self.base_url}/rest/v1/{endpoint}"
        
        async with httpx.AsyncClient() as client:
            if method == "GET":
                response = await client.get(url, headers=self.headers)
            elif method == "POST":
                response = await client.post(url, headers=self.headers, json=data)
            elif method == "PUT":
                response = await client.put(url, headers=self.headers, json=data)
            elif method == "DELETE":
                response = await client.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Método {method} não suportado")
            
            response.raise_for_status()
            return response.json() if response.content else {}
    
    # Métodos para Contas
    async def create_conta(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova conta"""
        result = await self._make_request("POST", "contas", data)
        return result[0] if result else None
    
    async def get_conta_by_id(self, conta_id: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter conta por ID"""
        result = await self._make_request("GET", f"contas?id=eq.{conta_id}")
        return result[0] if result else None
    
    async def get_conta_by_documento(self, documento: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter conta por documento"""
        result = await self._make_request("GET", f"contas?documento=eq.{documento}")
        return result[0] if result else None
    
    async def get_all_contas(self) -> List[Dict[str, Any]]:
        """AI dev note: Obter todas as contas"""
        return await self._make_request("GET", "contas")
    
    async def update_conta(self, conta_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar conta"""
        result = await self._make_request("PUT", f"contas?id=eq.{conta_id}", data)
        return result[0] if result else None
    
    async def delete_conta(self, conta_id: str) -> bool:
        """AI dev note: Deletar conta"""
        try:
            await self._make_request("DELETE", f"contas?id=eq.{conta_id}")
            return True
        except:
            return False
    
    # Métodos para Corretores
    async def create_corretor(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar novo corretor"""
        result = await self._make_request("POST", "corretores", data)
        return result[0] if result else None
    
    async def get_corretor_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter corretor por email"""
        result = await self._make_request("GET", f"corretores?email=eq.{email}")
        return result[0] if result else None
    
    async def get_corretores_by_conta(self, conta_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter corretores de uma conta"""
        return await self._make_request("GET", f"corretores?conta_id=eq.{conta_id}")
    
    async def update_corretor(self, corretor_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar corretor"""
        result = await self._make_request("PUT", f"corretores?id=eq.{corretor_id}", data)
        return result[0] if result else None
    
    async def delete_corretor(self, corretor_id: str) -> bool:
        """AI dev note: Deletar corretor"""
        try:
            await self._make_request("DELETE", f"corretores?id=eq.{corretor_id}")
            return True
        except:
            return False
    
    # Métodos para Clientes
    async def create_cliente(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar novo cliente"""
        result = await self._make_request("POST", "clientes", data)
        return result[0] if result else None
    
    async def get_clientes_by_conta(self, conta_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter clientes de uma conta"""
        return await self._make_request("GET", f"clientes?conta_id=eq.{conta_id}")
    
    async def get_cliente_by_id(self, cliente_id: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter cliente por ID"""
        result = await self._make_request("GET", f"clientes?id=eq.{cliente_id}")
        return result[0] if result else None
    
    async def update_cliente(self, cliente_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar cliente"""
        result = await self._make_request("PUT", f"clientes?id=eq.{cliente_id}", data)
        return result[0] if result else None
    
    async def delete_cliente(self, cliente_id: str) -> bool:
        """AI dev note: Deletar cliente"""
        try:
            await self._make_request("DELETE", f"clientes?id=eq.{cliente_id}")
            return True
        except:
            return False
    
    # Métodos para Conversas
    async def create_conversa(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova conversa"""
        result = await self._make_request("POST", "conversas", data)
        return result[0] if result else None
    
    async def get_conversas_by_cliente(self, cliente_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter conversas de um cliente"""
        return await self._make_request("GET", f"conversas?cliente_id=eq.{cliente_id}")
    
    async def update_conversa(self, conversa_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar conversa"""
        result = await self._make_request("PUT", f"conversas?id=eq.{conversa_id}", data)
        return result[0] if result else None
    
    async def delete_conversa(self, conversa_id: str) -> bool:
        """AI dev note: Deletar conversa"""
        try:
            await self._make_request("DELETE", f"conversas?id=eq.{conversa_id}")
            return True
        except:
            return False
    
    # Métodos para Mensagens
    async def create_mensagem(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova mensagem"""
        result = await self._make_request("POST", "mensagens", data)
        return result[0] if result else None
    
    async def get_mensagens_by_conversa(self, conversa_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter mensagens de uma conversa"""
        return await self._make_request("GET", f"mensagens?conversa_id=eq.{conversa_id}&order=timestamp.asc")
    
    async def update_mensagem_embedding(self, mensagem_id: str, embedding: List[float]) -> Dict[str, Any]:
        """AI dev note: Atualizar embedding de uma mensagem"""
        data = {"embedding_vetorial": embedding}
        result = await self._make_request("PUT", f"mensagens?id=eq.{mensagem_id}", data)
        return result[0] if result else None
    
    async def update_mensagem(self, mensagem_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar mensagem"""
        result = await self._make_request("PUT", f"mensagens?id=eq.{mensagem_id}", data)
        return result[0] if result else None
    
    async def delete_mensagem(self, mensagem_id: str) -> bool:
        """AI dev note: Deletar mensagem"""
        try:
            await self._make_request("DELETE", f"mensagens?id=eq.{mensagem_id}")
            return True
        except:
            return False
    
    # Métodos para Dossiês IA
    async def create_or_update_dossie(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar ou atualizar dossiê IA"""
        cliente_id = data.get('cliente_id')
        if not cliente_id:
            raise ValueError("cliente_id é obrigatório")
        
        # Verificar se já existe
        existing = await self._make_request("GET", f"dossies_ia?cliente_id=eq.{cliente_id}")
        
        if existing:
            # Atualizar
            result = await self._make_request("PUT", f"dossies_ia?cliente_id=eq.{cliente_id}", data)
        else:
            # Criar
            result = await self._make_request("POST", "dossies_ia", data)
        
        return result[0] if result else None
    
    async def get_dossie_by_cliente(self, cliente_id: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter dossiê de um cliente"""
        result = await self._make_request("GET", f"dossies_ia?cliente_id=eq.{cliente_id}")
        return result[0] if result else None
    
    async def update_dossie(self, dossie_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar dossiê IA"""
        result = await self._make_request("PUT", f"dossies_ia?id=eq.{dossie_id}", data)
        return result[0] if result else None
    
    async def delete_dossie(self, dossie_id: str) -> bool:
        """AI dev note: Deletar dossiê IA"""
        try:
            await self._make_request("DELETE", f"dossies_ia?id=eq.{dossie_id}")
            return True
        except:
            return False
    
    # Métodos para Lembretes
    async def create_lembrete(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar novo lembrete"""
        result = await self._make_request("POST", "lembretes", data)
        return result[0] if result else None
    
    async def get_lembretes_by_corretor(self, corretor_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter lembretes de um corretor"""
        return await self._make_request("GET", f"lembretes?corretor_id=eq.{corretor_id}&order=data_lembrete.asc")
    
    async def update_lembrete(self, lembrete_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar lembrete"""
        result = await self._make_request("PUT", f"lembretes?id=eq.{lembrete_id}", data)
        return result[0] if result else None
    
    async def delete_lembrete(self, lembrete_id: str) -> bool:
        """AI dev note: Deletar lembrete"""
        try:
            await self._make_request("DELETE", f"lembretes?id=eq.{lembrete_id}")
            return True
        except:
            return False
    
    # Métodos para Assinaturas
    async def create_assinatura(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova assinatura"""
        result = await self._make_request("POST", "assinaturas", data)
        return result[0] if result else None
    
    async def get_assinatura_by_conta(self, conta_id: str) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter assinatura de uma conta"""
        result = await self._make_request("GET", f"assinaturas?conta_id=eq.{conta_id}")
        return result[0] if result else None
    
    async def update_assinatura(self, assinatura_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar assinatura"""
        result = await self._make_request("PUT", f"assinaturas?id=eq.{assinatura_id}", data)
        return result[0] if result else None
    
    async def delete_assinatura(self, assinatura_id: str) -> bool:
        """AI dev note: Deletar assinatura"""
        try:
            await self._make_request("DELETE", f"assinaturas?id=eq.{assinatura_id}")
            return True
        except:
            return False
    
    # Métodos para Faturas
    async def create_fatura(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova fatura"""
        result = await self._make_request("POST", "faturas", data)
        return result[0] if result else None
    
    async def get_faturas_by_assinatura(self, assinatura_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter faturas de uma assinatura"""
        return await self._make_request("GET", f"faturas?assinatura_id=eq.{assinatura_id}&order=data_vencimento.desc")
    
    async def update_fatura(self, fatura_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar fatura"""
        result = await self._make_request("PUT", f"faturas?id=eq.{fatura_id}", data)
        return result[0] if result else None
    
    async def delete_fatura(self, fatura_id: str) -> bool:
        """AI dev note: Deletar fatura"""
        try:
            await self._make_request("DELETE", f"faturas?id=eq.{fatura_id}")
            return True
        except:
            return False
    
    # Métodos para Conexões Externas
    async def create_conexao_externa(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """AI dev note: Criar nova conexão externa"""
        result = await self._make_request("POST", "conexoes_externas", data)
        return result[0] if result else None
    
    async def get_conexoes_by_conta(self, conta_id: str) -> List[Dict[str, Any]]:
        """AI dev note: Obter conexões de uma conta"""
        return await self._make_request("GET", f"conexoes_externas?conta_id=eq.{conta_id}")
    
    async def update_conexao_externa(self, conexao_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar conexão externa"""
        result = await self._make_request("PUT", f"conexoes_externas?id=eq.{conexao_id}", data)
        return result[0] if result else None
    
    async def delete_conexao_externa(self, conexao_id: str) -> bool:
        """AI dev note: Deletar conexão externa"""
        try:
            await self._make_request("DELETE", f"conexoes_externas?id=eq.{conexao_id}")
            return True
        except:
            return False
    
    # Métodos para Planos
    async def get_planos_ativos(self) -> List[Dict[str, Any]]:
        """AI dev note: Obter planos ativos"""
        return await self._make_request("GET", "planos?is_ativo=eq.true")
    
    async def get_plano_by_id(self, plano_id: int) -> Optional[Dict[str, Any]]:
        """AI dev note: Obter plano por ID"""
        result = await self._make_request("GET", f"planos?id=eq.{plano_id}")
        return result[0] if result else None
    
    async def update_plano(self, plano_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """AI dev note: Atualizar plano"""
        result = await self._make_request("PUT", f"planos?id=eq.{plano_id}", data)
        return result[0] if result else None
    
    async def delete_plano(self, plano_id: int) -> bool:
        """AI dev note: Deletar plano"""
        try:
            await self._make_request("DELETE", f"planos?id=eq.{plano_id}")
            return True
        except:
            return False


# Instância global do serviço
supabase_service = SupabaseService() 