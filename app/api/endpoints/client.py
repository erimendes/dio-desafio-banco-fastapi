# app/api/endpoints/client.py
from app.db.database import get_db
from app.schemas.client import ClientCreate
from app.services.client import ClientService
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_current_user # Dependência JWT

from app.schemas.user import UserInDB

router = APIRouter(prefix="/clients", tags=["Client"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_client(
    client_data: ClientCreate,
    db: AsyncSession = Depends(get_db),
    # 1. Injeta o usuário autenticado (UserInDB)
    current_user: UserInDB = Depends(get_current_user) 
):
    # 2. A lógica de chamada para o Service
    return await ClientService.create_client(
        session=db, 
        name=client_data.name, 
        email=client_data.email, 
        # Passa o ID obtido do token:
        user_id=current_user.id 
    )