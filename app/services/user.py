# app/services/user.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.tables.user import User
from app.core.security import get_password_hash, verify_password # ⭐️ Importado verify_password
from databases import Database # Importe o objeto Databases para autenticação Core

class UserService:

    @staticmethod
    async def create_user(session: AsyncSession, username: str, email: str, password: str):
        hashed_password = get_password_hash(password)
        user = User(username=username, email=email, hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    @staticmethod
    async def get_user_by_username(session: AsyncSession, username: str):
        result = await session.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
    @staticmethod
    async def get_user_by_email(session: AsyncSession, email: str):
        result = await session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()      
    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int):
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    @staticmethod
    async def get_all_users(session: AsyncSession):
        result = await session.execute(select(User))
        return result.scalars().all()
    @staticmethod
    async def delete_user(session: AsyncSession, user: User):
        await session.delete(user)
        await session.commit()
    @staticmethod
    async def update_user_email(session: AsyncSession, user: User, new_email: str):
        user.email = new_email
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    @staticmethod   
    async def update_user_password(session: AsyncSession, user: User, new_password: str):
        hashed_password = get_password_hash(new_password)
        user.hashed_password = hashed_password
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user     
    @staticmethod   
    async def authenticate_user(session: AsyncSession, username: str, password: str):
        user = await UserService.get_user_by_username(session, username)
        if user and user.verify_password(password):
            return user
        return None
    @staticmethod   
    async def set_user_active_status(session: AsyncSession, user: User, is_active: bool):
        user.is_active = is_active
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    @staticmethod   
    async def set_user_superuser_status(session: AsyncSession, user: User, is_superuser: bool):
        user.is_superuser = is_superuser
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user 
    @staticmethod   
    async def update_profile_picture(session: AsyncSession, user: User, profile_picture_url: str):
        user.profile_picture = profile_picture_url
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user 
    @staticmethod   
    async def update_bio(session: AsyncSession, user: User, bio: str):
        user.bio = bio
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user 
    @staticmethod   
    async def update_location(session: AsyncSession, user: User, location: str):
        user.location = location
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user 
    
# FUNÇÕES EXTERNAS (Core/Autenticação Simples) 

# A função de autenticação que será chamada pelo endpoint /auth/token
# Esta função pode ser síncrona ou usar SQLAlchemy Core/Databases
async def authenticate_user(session: AsyncSession, username: str, password: str):
    
    # 1. Busca o usuário usando a sessão ORM
    user = await UserService.get_user_by_username(session, username)
    
    if user:
        # 2. Usa a função de segurança importada
        if verify_password(password, user.hashed_password):
             return user
             
    return None
