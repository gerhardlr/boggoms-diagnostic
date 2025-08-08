

from fastapi import FastAPI
from pydantic import BaseModel
from helpers.logging_config import get_logging_config
from helpers.db import get_db
from typing import Literal, Optional

from helpers import config

app = FastAPI()

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


class RequestData(BaseModel):
    type_id: Literal["RequestData"]
    path: str
    source: str
    timestamp: str


class Event(BaseModel):
    name: str
    ts: Optional[int | None] = None
    id: Optional[str | None] = None
    data: Optional[RequestData | None | dict] = None
    user: Optional[dict | None] = None
    v: Optional[str | None] = None


@app.post("/api/")
def post_event(event: Event):
    channel = config.get_channel()
    logger.info(f'pushing event{event}')
    return channel.consume(event)


@app.get("/api/")
def get_event():
    db = get_db()
    if result := db.ping():
        return {"message": f'DB is available with ping result: {result}'}
    return {"warning": f'DB is not available'}


@app.get("/")
def get_event_root():
    db = get_db()
    if result := db.ping():
        return {"message": f'DB is available with ping result: {result}'}
    return {"warning": f'DB is not available'}
