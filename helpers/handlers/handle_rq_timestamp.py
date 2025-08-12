from datetime import datetime

from helpers.topics import timestamp
from helpers.db import get_db
from ._base import base
from ._config import config


class StoreRequestTimeStamp(base.Consumer[timestamp.DataType]):

    def push_event(self, event: timestamp.DataType):
        db = get_db()
        date_str = datetime.fromtimestamp(
            int(event.timestamp)/1000).date().isoformat()
        db.push_event(date_str, event.data)
        db.inc(f'{date_str}_count')
        db.append_to_set("dates", date_str)


def register_self():
    handler = StoreRequestTimeStamp()
    config.subscribe(handler, timestamp.Topic)
