# app/db/tables/transaction.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String(20), nullable=False)  # ex: 'deposit', 'withdrawal', 'transfer'
    timestamp = Column(DateTime, default=datetime.utcnow)

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)

    # ✅ Relacionamento reverso com Account
    account = relationship("Account", back_populates="transactions")
    created_at = Column(DateTime, default=datetime.utcnow)