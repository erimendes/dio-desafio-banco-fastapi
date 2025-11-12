# app/services/transaction.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.tables.transaction import Transaction
from app.db.tables.account import Account

class TransactionService:

    @staticmethod
    async def create_transaction(session: AsyncSession, account_id: int, amount: float, type: str):
        # Atualiza saldo
        account = await session.get(Account, account_id)
        if not account:
            return None

        if type == "debit" and account.balance < amount:
            raise ValueError("Saldo insuficiente")
        if type == "debit":
            account.balance -= amount
        else:
            account.balance += amount

        transaction = Transaction(account_id=account_id, amount=amount, type=type)
        session.add(transaction)
        await session.commit()
        await session.refresh(transaction)
        return transaction

    @staticmethod
    async def get_transactions_by_account(session: AsyncSession, account_id: int):
        result = await session.execute(select(Transaction).where(Transaction.account_id == account_id))
        return result.scalars().all()
