# app/schemas/auth.py
from pydantic import BaseModel

# Schema de entrada para login
class LoginIn(BaseModel):
    username: str
    password: str

# ⭐️ Schema de saída para o token
class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"