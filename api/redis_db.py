import os
from datetime import datetime, timezone
import redis

redis_url = os.environ["REDIS_URL"]
password = os.environ["REDIS_PASSWORD"]
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
