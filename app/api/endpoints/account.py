# app/api/endpoints/account.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.account import AccountCreate, AccountRead
from app.services.account import AccountService
from app.db.database import get_db # Assumindo que get_db é a dependência para AsyncSession

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.post("/", response_model=AccountRead, status_code=201)
async def create_account(account: AccountCreate, db: AsyncSession = Depends(get_db)):
    
    return await AccountService.create_account(
        session=db, 
        client_id=account.client_id, 
        initial_balance=account.balance # Passando account.balance como initial_balance
    )
