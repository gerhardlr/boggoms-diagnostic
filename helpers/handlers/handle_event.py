from typing import cast
from ._base import base
from ._data_types import data_types
from ._config import config
from helpers.topics import request

_producer = None


class HandleEvent(base.Producer[request.RequestData]):

    def push(self, event: data_types.Event):
        if data := event.data:
            if isinstance(data, dict):
                if type_id := data.get("type_id"):
                    if type_id == "RequestData":
                        data = cast(request.RequestData, data)
                        self._push_event(data)


def register_self():
    global _producer
    _producer = HandleEvent()
    config.register(_producer, request.Requests)


def get_producer():
    assert _producer
    return _producer
