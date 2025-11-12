# app/schemas/client.py

from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str

class ClientRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
