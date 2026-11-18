from fastapi import FastAPI
from routers import users
from routers import accounts

app=FastAPI()

app.include_router(users.router)
app.include_router(accounts.router)
@app.get("/home")
def greet():
    return {"Welcome to our banking service":"Hey!"}
