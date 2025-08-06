import os
from datetime import datetime, timezone
from typing import Any
import redis

from .base import DB


class DBImpl(DB):

    def __init__(self):
        password = os.getenv("REDIS_PASSWORD")
        redis_host = os.getenv("REDIS_HOST", 'aware-javelin-17967.upstash.io')
        self._redis_db = redis.Redis(
            host=redis_host,
            port=6379,
            password=password,
            ssl=True
        )

    def push_event(self, event_name: str, event: Any):
        self._redis_db.lpush(event_name, event)


def get_db():
    return DBImpl()
