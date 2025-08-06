

from fastapi import FastAPI
from helpers.logging_config import get_logging_config

from helpers import config

app = FastAPI()

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


@app.post("/api/")
def post_event(event):
    channel = config.get_channel()
    logger.info('pushing event{event}')
    return channel.consume(event)


@app.get("/api/")
def get_event():
    logger.info('api/ got called')
    return {}
