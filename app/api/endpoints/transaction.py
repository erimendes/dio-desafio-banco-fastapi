# app/api/endpoints/transaction.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.transaction import TransactionCreate, TransactionRead
from app.services.transaction import TransactionService
from app.db.database import get_db

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionRead)
async def create_transaction(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    try:
        tx = await TransactionService.create_transaction(db, transaction.account_id, transaction.amount, transaction.type)
        if not tx:
            raise HTTPException(status_code=404, detail="Conta não encontrada")
        return tx
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
