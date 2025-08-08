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
        password = os.getenv("REDIS_PASSWORD")
        redis_host = os.getenv("REDIS_HOST", 'model-mastiff-18919.upstash.io')
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
            return self._redis_db.ping()
        except Exception as e:
            logger.exception(e)


def get_db():
    return DBImpl()
