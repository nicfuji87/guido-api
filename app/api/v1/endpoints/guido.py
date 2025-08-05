# AI dev note: Endpoints específicos para o sistema Guido
# Endpoints para gerenciar contas, corretores, clientes, etc.

from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.services.supabase_service import supabase_service
from app.schemas.guido import (
    ContaCreate, ContaResponse, ContaUpdate,
    CorretorCreate, CorretorResponse, CorretorUpdate,
    ClienteCreate, ClienteResponse, ClienteUpdate,
    ConversaCreate, ConversaResponse, ConversaUpdate,
    MensagemCreate, MensagemResponse, MensagemUpdate,
    LembreteCreate, LembreteResponse, LembreteUpdate,
    DossieIACreate, DossieIAResponse, DossieIAUpdate
)

router = APIRouter()


# Endpoints para Contas
@router.post("/contas", response_model=ContaResponse)
async def criar_conta(conta: ContaCreate):
    """AI dev note: Criar nova conta"""
    try:
        data = conta.dict()
        result = await supabase_service.create_conta(data)
        if result:
            return ContaResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar conta")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/contas", response_model=List[ContaResponse])
async def listar_todas_contas():
    """AI dev note: Listar todas as contas"""
    try:
        results = await supabase_service.get_all_contas()
        return [ContaResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/contas/{conta_id}", response_model=ContaResponse)
async def obter_conta(conta_id: str):
    """AI dev note: Obter conta por ID"""
    try:
        result = await supabase_service.get_conta_by_id(conta_id)
        if result:
            return ContaResponse(**result)
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/contas/{conta_id}", response_model=ContaResponse)
async def atualizar_conta(conta_id: str, conta: ContaUpdate):
    """AI dev note: Atualizar conta"""
    try:
        data = conta.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_conta(conta_id, data)
        if result:
            return ContaResponse(**result)
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/contas/{conta_id}")
async def deletar_conta(conta_id: str):
    """AI dev note: Deletar conta"""
    try:
        success = await supabase_service.delete_conta(conta_id)
        if success:
            return {"message": "Conta deletada com sucesso"}
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Corretores
@router.post("/corretores", response_model=CorretorResponse)
async def criar_corretor(corretor: CorretorCreate):
    """AI dev note: Criar novo corretor"""
    try:
        data = corretor.dict()
        result = await supabase_service.create_corretor(data)
        if result:
            return CorretorResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar corretor")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/corretores/conta/{conta_id}", response_model=List[CorretorResponse])
async def obter_corretores_conta(conta_id: str):
    """AI dev note: Obter corretores de uma conta"""
    try:
        results = await supabase_service.get_corretores_by_conta(conta_id)
        return [CorretorResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/corretores/{corretor_id}", response_model=CorretorResponse)
async def atualizar_corretor(corretor_id: str, corretor: CorretorUpdate):
    """AI dev note: Atualizar corretor"""
    try:
        data = corretor.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_corretor(corretor_id, data)
        if result:
            return CorretorResponse(**result)
        raise HTTPException(status_code=404, detail="Corretor não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/corretores/{corretor_id}")
async def deletar_corretor(corretor_id: str):
    """AI dev note: Deletar corretor"""
    try:
        success = await supabase_service.delete_corretor(corretor_id)
        if success:
            return {"message": "Corretor deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Corretor não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Clientes
@router.post("/clientes", response_model=ClienteResponse)
async def criar_cliente(cliente: ClienteCreate):
    """AI dev note: Criar novo cliente"""
    try:
        data = cliente.dict()
        result = await supabase_service.create_cliente(data)
        if result:
            return ClienteResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar cliente")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/clientes/conta/{conta_id}", response_model=List[ClienteResponse])
async def obter_clientes_conta(conta_id: str):
    """AI dev note: Obter clientes de uma conta"""
    try:
        results = await supabase_service.get_clientes_by_conta(conta_id)
        return [ClienteResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/clientes/{cliente_id}", response_model=ClienteResponse)
async def obter_cliente(cliente_id: str):
    """AI dev note: Obter cliente por ID"""
    try:
        result = await supabase_service.get_cliente_by_id(cliente_id)
        if result:
            return ClienteResponse(**result)
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/clientes/{cliente_id}", response_model=ClienteResponse)
async def atualizar_cliente(cliente_id: str, cliente: ClienteUpdate):
    """AI dev note: Atualizar cliente"""
    try:
        data = cliente.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_cliente(cliente_id, data)
        if result:
            return ClienteResponse(**result)
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/clientes/{cliente_id}")
async def deletar_cliente(cliente_id: str):
    """AI dev note: Deletar cliente"""
    try:
        success = await supabase_service.delete_cliente(cliente_id)
        if success:
            return {"message": "Cliente deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Conversas
@router.post("/conversas", response_model=ConversaResponse)
async def criar_conversa(conversa: ConversaCreate):
    """AI dev note: Criar nova conversa"""
    try:
        data = conversa.dict()
        result = await supabase_service.create_conversa(data)
        if result:
            return ConversaResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar conversa")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/conversas/cliente/{cliente_id}", response_model=List[ConversaResponse])
async def obter_conversas_cliente(cliente_id: str):
    """AI dev note: Obter conversas de um cliente"""
    try:
        results = await supabase_service.get_conversas_by_cliente(cliente_id)
        return [ConversaResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/conversas/{conversa_id}", response_model=ConversaResponse)
async def atualizar_conversa(conversa_id: str, conversa: ConversaUpdate):
    """AI dev note: Atualizar conversa"""
    try:
        data = conversa.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_conversa(conversa_id, data)
        if result:
            return ConversaResponse(**result)
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/conversas/{conversa_id}")
async def deletar_conversa(conversa_id: str):
    """AI dev note: Deletar conversa"""
    try:
        success = await supabase_service.delete_conversa(conversa_id)
        if success:
            return {"message": "Conversa deletada com sucesso"}
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Mensagens
@router.post("/mensagens", response_model=MensagemResponse)
async def criar_mensagem(mensagem: MensagemCreate):
    """AI dev note: Criar nova mensagem"""
    try:
        data = mensagem.dict()
        result = await supabase_service.create_mensagem(data)
        if result:
            return MensagemResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar mensagem")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/mensagens/conversa/{conversa_id}", response_model=List[MensagemResponse])
async def obter_mensagens_conversa(conversa_id: str):
    """AI dev note: Obter mensagens de uma conversa"""
    try:
        results = await supabase_service.get_mensagens_by_conversa(conversa_id)
        return [MensagemResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/mensagens/{mensagem_id}", response_model=MensagemResponse)
async def atualizar_mensagem(mensagem_id: str, mensagem: MensagemUpdate):
    """AI dev note: Atualizar mensagem"""
    try:
        data = mensagem.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_mensagem(mensagem_id, data)
        if result:
            return MensagemResponse(**result)
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/mensagens/{mensagem_id}")
async def deletar_mensagem(mensagem_id: str):
    """AI dev note: Deletar mensagem"""
    try:
        success = await supabase_service.delete_mensagem(mensagem_id)
        if success:
            return {"message": "Mensagem deletada com sucesso"}
        raise HTTPException(status_code=404, detail="Mensagem não encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Lembretes
@router.post("/lembretes", response_model=LembreteResponse)
async def criar_lembrete(lembrete: LembreteCreate):
    """AI dev note: Criar novo lembrete"""
    try:
        data = lembrete.dict()
        result = await supabase_service.create_lembrete(data)
        if result:
            return LembreteResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar lembrete")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/lembretes/corretor/{corretor_id}", response_model=List[LembreteResponse])
async def obter_lembretes_corretor(corretor_id: str):
    """AI dev note: Obter lembretes de um corretor"""
    try:
        results = await supabase_service.get_lembretes_by_corretor(corretor_id)
        return [LembreteResponse(**result) for result in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/lembretes/{lembrete_id}", response_model=LembreteResponse)
async def atualizar_lembrete(lembrete_id: str, lembrete: LembreteUpdate):
    """AI dev note: Atualizar lembrete"""
    try:
        data = lembrete.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_lembrete(lembrete_id, data)
        if result:
            return LembreteResponse(**result)
        raise HTTPException(status_code=404, detail="Lembrete não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/lembretes/{lembrete_id}")
async def deletar_lembrete(lembrete_id: str):
    """AI dev note: Deletar lembrete"""
    try:
        success = await supabase_service.delete_lembrete(lembrete_id)
        if success:
            return {"message": "Lembrete deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Lembrete não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Dossiês IA
@router.post("/dossies-ia", response_model=DossieIAResponse)
async def criar_dossie_ia(dossie: DossieIACreate):
    """AI dev note: Criar ou atualizar dossiê IA"""
    try:
        data = dossie.dict()
        result = await supabase_service.create_or_update_dossie(data)
        if result:
            return DossieIAResponse(**result)
        raise HTTPException(status_code=400, detail="Erro ao criar dossiê")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/dossies-ia/cliente/{cliente_id}", response_model=DossieIAResponse)
async def obter_dossie_cliente(cliente_id: str):
    """AI dev note: Obter dossiê de um cliente"""
    try:
        result = await supabase_service.get_dossie_by_cliente(cliente_id)
        if result:
            return DossieIAResponse(**result)
        raise HTTPException(status_code=404, detail="Dossiê não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/dossies-ia/{dossie_id}", response_model=DossieIAResponse)
async def atualizar_dossie_ia(dossie_id: str, dossie: DossieIAUpdate):
    """AI dev note: Atualizar dossiê IA"""
    try:
        data = dossie.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar")
        
        result = await supabase_service.update_dossie(dossie_id, data)
        if result:
            return DossieIAResponse(**result)
        raise HTTPException(status_code=404, detail="Dossiê não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/dossies-ia/{dossie_id}")
async def deletar_dossie_ia(dossie_id: str):
    """AI dev note: Deletar dossiê IA"""
    try:
        success = await supabase_service.delete_dossie(dossie_id)
        if success:
            return {"message": "Dossiê deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Dossiê não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoints para Planos
@router.get("/planos", response_model=List[dict])
async def obter_planos_ativos():
    """AI dev note: Obter planos ativos"""
    try:
        results = await supabase_service.get_planos_ativos()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 