from app.db.database import transaction_context
from app.db.tables.user import User
from app.core.security import get_password_hash

with transaction_context() as db:
    user = User(
        username="admin",
        email="admin@example.com",
        hashed_password=get_password_hash("123456")
    )
    db.add(user)
    print("✅ Usuário criado com sucesso!")
