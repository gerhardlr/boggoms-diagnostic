import json
from typing import Dict, Any


from _types import VercelRequest
from .redis_db import ping_db


def handler(request: VercelRequest) -> Dict[str, Any]:

    timestamp = ping_db()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Ping logged",
            "timestamp": timestamp
        }),
    }
