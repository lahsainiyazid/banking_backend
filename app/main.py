from fastapi import FastAPI



app=FastAPI()


@app.get("/home")
def greet():
    return {"Welcome to our banking service":"Hey!"}
