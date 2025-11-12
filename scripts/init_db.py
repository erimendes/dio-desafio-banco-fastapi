# scripts/init_db.py
import asyncio
from app.db.database import engine
from app.db.base import Base
import app.db.base_models  # 👈 Importa todos os modelos

async def init_db():
    async with engine.begin() as conn:
        print("Criando tabelas no banco de dados...")
        await conn.run_sync(Base.metadata.create_all)
        print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(init_db())
