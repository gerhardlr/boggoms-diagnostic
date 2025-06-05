from typing import Union

from fastapi import FastAPI
from helpers.redis_db import ping_db

app = FastAPI()


@app.get("/api/")
def read_root():
    # return {"Hello": "World"}
    return ping_db()


@app.get("/api/ping")
def read_root():
    return {"Hello": "World"}
