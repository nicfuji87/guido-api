# AI dev note: Schemas Pydantic para usuário
# Usar Pydantic para validação e serialização de dados

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """AI dev note: Schema base para usuário"""
    email: EmailStr
    username: str
    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    """AI dev note: Schema para criação de usuário"""
    password: str


class UserUpdate(BaseModel):
    """AI dev note: Schema para atualização de usuário"""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None


class UserInDBBase(UserBase):
    """AI dev note: Schema base para usuário no banco de dados"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class User(UserInDBBase):
    """AI dev note: Schema para resposta de usuário (sem senha)"""
    pass


class UserInDB(UserInDBBase):
    """AI dev note: Schema para usuário no banco de dados (com senha)"""
    hashed_password: str 