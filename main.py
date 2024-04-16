from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"hello": "Hello Developers 4"}


@app.get("/status")
async def hello():
    return {"status": 401}
