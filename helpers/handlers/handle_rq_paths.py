from helpers.topics import request_path
from helpers.db import get_db
from ._base import base
from ._config import config


class StoreRequestPath(base.Consumer[request_path.Data]):

    def push_event(self, event: request_path.Data):
        db = get_db()
        db.push_event(event.name, event.data)
        db.inc(f'{event.name}_count')
        db.append_to_set("paths", event.name)


def register_self():
    request_source_handler = StoreRequestPath()
    config.subscribe(request_source_handler, request_path.Topic)
