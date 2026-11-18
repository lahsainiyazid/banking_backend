from fastapi import FastAPI
from routers import users


app=FastAPI()

app.include_router(users.router)
@app.get("/home")
def greet():
    return {"Welcome to our banking service":"Hey!"}
