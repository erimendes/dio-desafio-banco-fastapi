# app/db/tables/account.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    account_number = Column(String(20), unique=True, nullable=False)
    balance = Column(Float, default=0.0)

    # ✅ Relacionamento com Transaction
    transactions = relationship("Transaction", back_populates="account", cascade="all, delete-orphan")

    # Opcional: relacionamento com Client
    client = relationship("Client", back_populates="accounts")
