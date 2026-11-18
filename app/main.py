from fastapi import FastAPI
from routers.users import users
from routers.accounts import accounts 
from routers.transactions import transactions
app=FastAPI()

app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
@app.get("/home")
def greet():
    return {"Welcome to our banking service":"Hey!"}
