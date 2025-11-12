# app/schemas/transaction.py
from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    type: str  # 'credit' ou 'debit'

class TransactionRead(BaseModel):
    id: int
    account_id: int
    amount: float
    type: str
    created_at: datetime

    class Config:
        from_attributes = True
