"This is the main runner file of the project"

from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello():
    "This just returns greeting to developers"

    return {"hello": "Hello Developers 4"}


@app.get("/status")
async def status():
    "This is a status of the project"

    return {"status": 401}
