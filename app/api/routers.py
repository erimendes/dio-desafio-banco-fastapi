from app.api.endpoints import user, auth, account, client, transaction

def include_routers(app):
    app.include_router(user.router, prefix="/users", tags=["Users"])
    app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
    app.include_router(account.router, prefix="/accounts", tags=["Accounts"])
    app.include_router(client.router, prefix="/clients", tags=["Clients"])
    app.include_router(transaction.router, prefix="/transactions", tags=["Transactions"])
