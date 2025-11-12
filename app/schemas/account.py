# app/schemas/account.py
from pydantic import BaseModel

class AccountCreate(BaseModel):
    client_id: int
    account_number: str
    balance: float = 0.0

class AccountRead(BaseModel):
    id: int
    client_id: int
    account_number: str
    balance: float

    class Config:
        from_attributes = True
