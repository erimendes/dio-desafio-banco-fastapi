# app/services/client.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.tables.client import Client # Assumindo que este é o seu modelo ORM

class ClientService:

    @staticmethod
    async def create_client(
        session: AsyncSession, 
        name: str, 
        email: str,
        user_id: int 
    ):
        # USE o user_id na criação do objeto Client:
        client = Client(name=name, email=email, user_id=user_id) 
        
        session.add(client)
        
        try:
            await session.commit()
        except Exception as e:
            await session.rollback()
            # Tratamento de erro de integridade (ex: usuário já é cliente)
            # Você deve implementar um tratamento de IntegrityError aqui, mas por ora, re-lançamos:
            raise e 
            
        await session.refresh(client)
        return client

    # ... (outras funções do Service)

    @staticmethod
    async def get_client_by_id(session: AsyncSession, client_id: int):
        return await session.get(Client, client_id)