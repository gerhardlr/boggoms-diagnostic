import json
from unittest.mock import Mock
from .base import DB
import os
from typing import Any
import redis
from .logging_config import get_logging_config

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


class DBImpl(DB):

    def __init__(self):
        password = os.getenv("REDIS_PASS")
        redis_host = os.getenv("REDIS_HOST", 'model-mastiff-18919.upstash.io')
        self._credentials = (password, redis_host)
        self._redis_db = redis.Redis(
            host=redis_host,
            port=6379,
            password=password,
            ssl=True
        )

    def push_event(self, event_name: str, event: Any):
        if isinstance(event, dict):
            event = json.dumps(event)
        self._redis_db.lpush(event_name, event)

    def inc(self, key: str):
        self._redis_db.incr(key)

    def ping(self):
        try:
            # logger.info(self._credentials)
            return self._redis_db.ping()
        except Exception as e:
            logger.exception(e)
            logger.info(self._credentials)


def get_db():
    if os.getenv('DRY_RUN'):
        return Mock(spec=DB)
    return DBImpl()
