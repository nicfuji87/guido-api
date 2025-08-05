# AI dev note: Schemas Pydantic para o sistema Guido
# Schemas para todas as entidades do sistema

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, UUID4


# Schemas para Contas
class ContaBase(BaseModel):
    """AI dev note: Schema base para conta"""
    nome_conta: str
    tipo_conta: str  # 'IMOBILIARIA' ou 'INDIVIDUAL'
    documento: str


class ContaCreate(ContaBase):
    """AI dev note: Schema para criação de conta"""
    pass


class ContaUpdate(BaseModel):
    """AI dev note: Schema para atualização de conta"""
    nome_conta: Optional[str] = None
    tipo_conta: Optional[str] = None  # 'IMOBILIARIA' ou 'INDIVIDUAL'
    documento: Optional[str] = None


class ContaResponse(ContaBase):
    """AI dev note: Schema para resposta de conta"""
    id: UUID4
    data_criacao: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Corretores
class CorretorBase(BaseModel):
    """AI dev note: Schema base para corretor"""
    conta_id: UUID4
    nome: str
    email: EmailStr
    funcao: str  # 'DONO', 'ADMIN', 'AGENTE'


class CorretorCreate(CorretorBase):
    """AI dev note: Schema para criação de corretor"""
    hash_senha: str


class CorretorUpdate(BaseModel):
    """AI dev note: Schema para atualização de corretor"""
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    funcao: Optional[str] = None  # 'DONO', 'ADMIN', 'AGENTE'
    hash_senha: Optional[str] = None


class CorretorResponse(CorretorBase):
    """AI dev note: Schema para resposta de corretor (sem senha)"""
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Clientes
class ClienteBase(BaseModel):
    """AI dev note: Schema base para cliente"""
    conta_id: UUID4
    nome: str
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    status_funil: Optional[str] = None


class ClienteCreate(ClienteBase):
    """AI dev note: Schema para criação de cliente"""
    corretor_id: Optional[UUID4] = None


class ClienteUpdate(BaseModel):
    """AI dev note: Schema para atualização de cliente"""
    nome: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    status_funil: Optional[str] = None
    corretor_id: Optional[UUID4] = None


class ClienteResponse(ClienteBase):
    """AI dev note: Schema para resposta de cliente"""
    id: UUID4
    corretor_id: Optional[UUID4] = None
    data_criacao: datetime
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Conversas
class ConversaBase(BaseModel):
    """AI dev note: Schema base para conversa"""
    cliente_id: UUID4
    plataforma: str
    status_conversa: str  # 'AGUARDANDO_CORRETOR', 'AGUARDANDO_CLIENTE', 'FINALIZADA'


class ConversaCreate(ConversaBase):
    """AI dev note: Schema para criação de conversa"""
    pass


class ConversaUpdate(BaseModel):
    """AI dev note: Schema para atualização de conversa"""
    plataforma: Optional[str] = None
    status_conversa: Optional[str] = None  # 'AGUARDANDO_CORRETOR', 'AGUARDANDO_CLIENTE', 'FINALIZADA'


class ConversaResponse(ConversaBase):
    """AI dev note: Schema para resposta de conversa"""
    id: UUID4
    timestamp_ultima_mensagem: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Mensagens
class MensagemBase(BaseModel):
    """AI dev note: Schema base para mensagem"""
    conversa_id: UUID4
    remetente: str  # 'CORRETOR', 'CLIENTE', 'SISTEMA'
    conteudo_texto: str


class MensagemCreate(MensagemBase):
    """AI dev note: Schema para criação de mensagem"""
    pass


class MensagemUpdate(BaseModel):
    """AI dev note: Schema para atualização de mensagem"""
    remetente: Optional[str] = None  # 'CORRETOR', 'CLIENTE', 'SISTEMA'
    conteudo_texto: Optional[str] = None


class MensagemResponse(MensagemBase):
    """AI dev note: Schema para resposta de mensagem"""
    id: UUID4
    timestamp: datetime
    embedding_vetorial: Optional[List[float]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Lembretes
class LembreteBase(BaseModel):
    """AI dev note: Schema base para lembrete"""
    corretor_id: UUID4
    descricao: str
    data_lembrete: datetime
    status: str  # 'PENDENTE', 'CONCLUIDO'


class LembreteCreate(LembreteBase):
    """AI dev note: Schema para criação de lembrete"""
    cliente_id: Optional[UUID4] = None


class LembreteUpdate(BaseModel):
    """AI dev note: Schema para atualização de lembrete"""
    descricao: Optional[str] = None
    data_lembrete: Optional[datetime] = None
    status: Optional[str] = None  # 'PENDENTE', 'CONCLUIDO'
    cliente_id: Optional[UUID4] = None


class LembreteResponse(LembreteBase):
    """AI dev note: Schema para resposta de lembrete"""
    id: UUID4
    cliente_id: Optional[UUID4] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Dossiês IA
class DossieIABase(BaseModel):
    """AI dev note: Schema base para dossiê IA"""
    cliente_id: UUID4
    resumo_gerado: Optional[str] = None
    sentimento_geral: Optional[str] = None


class DossieIACreate(DossieIABase):
    """AI dev note: Schema para criação de dossiê IA"""
    pass


class DossieIAUpdate(BaseModel):
    """AI dev note: Schema para atualização de dossiê IA"""
    resumo_gerado: Optional[str] = None
    sentimento_geral: Optional[str] = None


class DossieIAResponse(DossieIABase):
    """AI dev note: Schema para resposta de dossiê IA"""
    id: UUID4
    ultima_atualizacao: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Assinaturas
class AssinaturaBase(BaseModel):
    """AI dev note: Schema base para assinatura"""
    conta_id: UUID4
    plano_id: int
    status: str  # 'TRIAL', 'ATIVO', 'PAGAMENTO_PENDENTE', 'CANCELADO'


class AssinaturaCreate(AssinaturaBase):
    """AI dev note: Schema para criação de assinatura"""
    data_fim_trial: Optional[datetime] = None
    data_proxima_cobranca: Optional[datetime] = None
    id_gateway_pagamento: Optional[str] = None


class AssinaturaUpdate(BaseModel):
    """AI dev note: Schema para atualização de assinatura"""
    plano_id: Optional[int] = None
    status: Optional[str] = None  # 'TRIAL', 'ATIVO', 'PAGAMENTO_PENDENTE', 'CANCELADO'
    data_fim_trial: Optional[datetime] = None
    data_proxima_cobranca: Optional[datetime] = None
    id_gateway_pagamento: Optional[str] = None


class AssinaturaResponse(AssinaturaBase):
    """AI dev note: Schema para resposta de assinatura"""
    id: UUID4
    data_fim_trial: Optional[datetime] = None
    data_proxima_cobranca: Optional[datetime] = None
    id_gateway_pagamento: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Faturas
class FaturaBase(BaseModel):
    """AI dev note: Schema base para fatura"""
    assinatura_id: UUID4
    valor: float
    status: str  # 'PENDENTE', 'PAGO', 'FALHOU', 'REEMBOLSADO'
    data_vencimento: datetime


class FaturaCreate(FaturaBase):
    """AI dev note: Schema para criação de fatura"""
    data_pagamento: Optional[datetime] = None
    url_documento: Optional[str] = None
    id_gateway_pagamento: Optional[str] = None


class FaturaUpdate(BaseModel):
    """AI dev note: Schema para atualização de fatura"""
    valor: Optional[float] = None
    status: Optional[str] = None  # 'PENDENTE', 'PAGO', 'FALHOU', 'REEMBOLSADO'
    data_vencimento: Optional[datetime] = None
    data_pagamento: Optional[datetime] = None
    url_documento: Optional[str] = None
    id_gateway_pagamento: Optional[str] = None


class FaturaResponse(FaturaBase):
    """AI dev note: Schema para resposta de fatura"""
    id: UUID4
    data_pagamento: Optional[datetime] = None
    url_documento: Optional[str] = None
    id_gateway_pagamento: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Conexões Externas
class ConexaoExternaBase(BaseModel):
    """AI dev note: Schema base para conexão externa"""
    conta_id: UUID4
    plataforma: str
    chave_api_criptografada: str
    status: str  # 'ATIVA', 'INATIVA', 'ERRO_AUTENTICACAO'


class ConexaoExternaCreate(ConexaoExternaBase):
    """AI dev note: Schema para criação de conexão externa"""
    pass


class ConexaoExternaUpdate(BaseModel):
    """AI dev note: Schema para atualização de conexão externa"""
    plataforma: Optional[str] = None
    chave_api_criptografada: Optional[str] = None
    status: Optional[str] = None  # 'ATIVA', 'INATIVA', 'ERRO_AUTENTICACAO'


class ConexaoExternaResponse(ConexaoExternaBase):
    """AI dev note: Schema para resposta de conexão externa"""
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Schemas para Planos
class PlanoBase(BaseModel):
    """AI dev note: Schema base para plano"""
    nome_plano: str
    codigo_externo: str
    preco_mensal: float
    preco_anual: Optional[float] = None
    limite_corretores: int
    descricao: Optional[str] = None
    is_ativo: bool = True


class PlanoCreate(PlanoBase):
    """AI dev note: Schema para criação de plano"""
    pass


class PlanoUpdate(BaseModel):
    """AI dev note: Schema para atualização de plano"""
    nome_plano: Optional[str] = None
    codigo_externo: Optional[str] = None
    preco_mensal: Optional[float] = None
    preco_anual: Optional[float] = None
    limite_corretores: Optional[int] = None
    descricao: Optional[str] = None
    is_ativo: Optional[bool] = None


class PlanoResponse(PlanoBase):
    """AI dev note: Schema para resposta de plano"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 