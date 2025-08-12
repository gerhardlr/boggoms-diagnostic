

from fastapi import FastAPI

from helpers import get_root
from helpers.logging_config import get_logging_config
from helpers.db import get_db
from helpers.data_types import Event


app = FastAPI()

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


@app.post("/api/")
def post_event(event: Event):
    root = get_root()
    logger.info(f'pushing event{event}')
    return root.push(event)


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
