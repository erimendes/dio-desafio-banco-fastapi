# app/api/endpoints/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession # Necessário para o Depends(get_db)
from app.db.database import get_db
from app.schemas.auth import TokenOut
from app.services.user import authenticate_user
from app.core.security import create_access_token
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=TokenOut)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), # Captura username e password
    session: AsyncSession = Depends(get_db)
):
    # O Controller agora recebe form_data.username e form_data.password
    
    # 1. Autenticação (Lógica de Serviço)
    user = await authenticate_user(session, form_data.username, form_data.password) 

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # 2. Criação do Token
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}