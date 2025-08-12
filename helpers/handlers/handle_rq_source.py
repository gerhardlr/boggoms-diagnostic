from helpers.topics import request_source
from helpers.db import get_db
from ._base import base
from ._config import config


class StoreRequesSource(base.Consumer[request_source.DataType]):

    def push_event(self, event: request_source.DataType):
        db = get_db()
        db.push_event(event.name, event.data)
        db.inc(event.name)
        db.append_to_set("sources", event.name)


def register_self():
    request_source_handler = StoreRequesSource()
    config.subscribe(request_source_handler, request_source.Topic)
