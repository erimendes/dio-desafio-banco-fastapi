# app/core/security.py
from datetime import datetime, timedelta, timezone
from typing import Union
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db # Gerador assíncrono

# Importação local para o schema do usuário
from app.schemas.user import UserInDB 

# --- CONFIGURAÇÃO DE SENHA (ARGON2) ---
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Gera o hash da senha com Argon2."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica senha com Argon2."""
    return pwd_context.verify(plain_password, hashed_password)


# --- CONFIGURAÇÃO JWT ---
SECRET_KEY = "SUA_CHAVE_SECRETA_MUITO_LONGA_E_RANDOMICA"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    """Cria um novo token JWT."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    
    to_encode.update({"exp": expire, "sub": data.get("sub")})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# --- FUNÇÃO DE DEPENDÊNCIA (Quebra a Circularidade) ---
async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    from app.services.user import UserService  # ✅ Import local para evitar circularidade

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 1️⃣ Obtém sessão do banco
    try:
        session: AsyncSession = await anext(get_db()) 
    except StopAsyncIteration:
        raise HTTPException(status_code=500, detail="Database connection error during authentication setup")

    # 2️⃣ Busca o usuário
    try:
        user = await UserService.get_user_by_username(
            session=session,
            username=username
        )
        if user is None:
            raise credentials_exception

        return UserInDB.model_validate(user)
    finally:
        try:
            await anext(get_db())
        except StopAsyncIteration:
            pass
