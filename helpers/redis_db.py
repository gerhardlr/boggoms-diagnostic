import os
from datetime import datetime, timezone
import redis

password = os.getenv("REDIS_PASSWORD")
redis_db = redis.Redis(
    host='aware-javelin-17967.upstash.io',
    port=6379,
    password=password,
    ssl=True
)


def ping_db():
    timestamp = datetime.now(timezone.utc).isoformat()
    redis_db.lpush("ping_log", timestamp)
    return timestamp
