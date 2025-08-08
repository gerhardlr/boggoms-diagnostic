from .base import DB
import os
from datetime import datetime, timezone
from typing import Any
import redis
from .logging_config import get_logging_config

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


class DBImpl(DB):

    def __init__(self):
        # s.getenv("REDIS_PASSWORD")
        password = "AUnnAAIjcDFkM2NlMGJhYmEyNjI0MDIwYTMxYjNhMGU4NGU1N2NjNnAxMA"
        redis_host = os.getenv("REDIS_HOST", 'model-mastiff-18919.upstash.io')
        self._credentials = (password, redis_host)
        self._redis_db = redis.Redis(
            host=redis_host,
            port=6379,
            password=password,
            ssl=True
        )

    def push_event(self, event_name: str, event: Any):
        self._redis_db.lpush(event_name, event)

    def ping(self):
        try:
            # logger.info(self._credentials)
            return self._redis_db.ping()
        except Exception as e:
            logger.exception(e)
            logger.info(self._credentials)


def get_db():
    return DBImpl()
