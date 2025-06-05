import json
import os
from datetime import datetime, timezone
from typing import Dict, Any
import redis

from _types import VercelRequest

redis_url = os.environ["REDIS_URL"]
r = redis.from_url(redis_url)


def handler(request: VercelRequest) -> Dict[str, Any]:
    timestamp = datetime.now(timezone.utc).isoformat()
    r.lpush("ping_log", timestamp)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Ping logged",
            "timestamp": timestamp
        }),
    }
