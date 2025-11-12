# app/schemas/user.py
from pydantic import BaseModel, Field # ⭐️ Importe Field
from typing import Optional

# --- Schemas para Criação e Leitura ---

class UserCreate(BaseModel):
    """Schema de entrada para criação de um novo usuário."""
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=100)
    
    # Limite de 72 caracteres para evitar o erro do bcrypt.
    password: str = Field(..., min_length=8, max_length=72) 


class UserRead(BaseModel):
    """Schema de saída para exibir dados do usuário (sem a senha)."""
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# --- Schemas de Suporte (Descomentei e corrigi a sintaxe) ---

class UserInDB(BaseModel):
    """Schema interno que inclui o hash da senha, usado pela camada Service/DB."""
    id: int
    username: str
    email: str
    hashed_password: str # Campo crucial

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """Schema de atualização, todos os campos opcionais."""
    # Uso de Optional para campos que podem ser nulos e não precisam ser enviados.
    email: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=72)
    
    # Exemplo de outros campos:
    full_name: Optional[str] = None
    is_active: Optional[bool] = None # Boas práticas: use bool em vez de int (0/1)

    class Config:
        from_attributes = True