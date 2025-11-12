# app/db/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./bank.db")

# Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # log SQL
    future=True
)

# Async Session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency para FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
