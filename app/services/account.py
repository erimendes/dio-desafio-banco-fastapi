# app/services/account.py
import random
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.tables.account import Account # ⭐️ Importe a classe ORM Account
from app.core.exceptions import BusinessError 

class AccountService:

    @staticmethod
    async def _generate_unique_account_number(session: AsyncSession) -> str:
        """ Gera um número de conta aleatório de 10 dígitos e verifica a unicidade. """
        while True:
            # Gera um número aleatório de 10 dígitos (ajuste o formato conforme necessário)
            account_number = "".join([str(random.randint(0, 9)) for _ in range(10)])
            
            # Consulta para verificar se o número já existe no DB
            stmt = select(Account).where(Account.account_number == account_number)
            result = await session.execute(stmt)
            
            # Se não houver resultado, o número é único
            if result.scalars().first() is None:
                return account_number

    @staticmethod
    async def create_account(session: AsyncSession, client_id: int, initial_balance: float = 0.0):
        """
        Cria uma nova conta, gerando um número único e associando-a a um cliente.
        
        Note: O AccountService NÃO deve receber account_number na entrada, mas sim gerá-lo.
        """
        # 1. Lógica de Negócio: Garantir que o cliente não tenha conta duplicada
        #    (Se a coluna 'client_id' for UNIQUE no DB, o DB fará a checagem. 
        #    Aqui, estamos assumindo que o cliente_id vem do usuário autenticado.)
        
        # 2. Gera um número único para a nova conta
        unique_number = await AccountService._generate_unique_account_number(session)

        # 3. Cria e adiciona o objeto Account
        account = Account(
            client_id=client_id, 
            account_number=unique_number, 
            balance=initial_balance
        )
        session.add(account)
        
        # 4. Persiste no DB
        try:
            await session.commit()
        except sa.exc.IntegrityError:
             # Lança erro de negócio se o client_id já tiver uma conta
             await session.rollback()
             raise BusinessError("Este cliente já possui uma conta bancária registrada.")

        await session.refresh(account)
        return account

    @staticmethod
    async def get_account_by_id(session: AsyncSession, account_id: int):
        """ Busca uma conta pelo ID. """
        return await session.get(Account, account_id)