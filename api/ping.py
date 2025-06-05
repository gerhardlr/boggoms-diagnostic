from fastapi import FastAPI
from helpers.redis_db import ping_db

app = FastAPI()


@app.post("/api/ping")
def read_root():
    return ping_db()
