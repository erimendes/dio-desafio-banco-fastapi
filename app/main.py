from fastapi import FastAPI
from app.api.endpoints import user, account, client, transaction, auth
from app.api import routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Banco FastAPI Async",
    version="1.0.0",
    description="""
API assíncrona para gerenciamento bancário com FastAPI e SQLAlchemy AsyncIO.
## No Banco FastAPI Async
Você será capaz de:
* **Cadastrar usuários**.
* **Gerar token**.
* **Criar conta**.
* **Cadastrar cliente**.
* **Fazer movimentações de débito e crédito**.
""",
)

# app.include_router(user.router)
# app.include_router(auth.router)
# app.include_router(account.router)
# app.include_router(client.router)
# app.include_router(transaction.router)

# Middleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

# Inclui todos os routers
routers.include_routers(app)