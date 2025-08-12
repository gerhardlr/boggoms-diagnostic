from helpers.topics import request_source, request, request_path, timestamp
from ._base import base
from ._data_types import data_types
from ._config import config


class HandleRequestToSource(
    base.Consumer[request.RequestData],
    base.Producer[request_source.DataType]
):

    def push_event(self, event: data_types.RequestData):
        eventsource = request_source.DataType(
            event['source'], request_source.RequestSourceData(
                path=event['path'],
                timestamp=event['timestamp']
            )
        )
        self._push_event(eventsource)


class HandleRequestToPath(base.Consumer[request.RequestData], base.Producer[request_path.RequestPathTuple]):

    def push_event(self, event: data_types.RequestData):
        eventpath = request_path.RequestPathTuple(
            event['path'], request_path.RequestPathData(
                source=event['source'],
                timestamp=event['timestamp']
            )
        )
        self._push_event(eventpath)


class HandleRequestToTimeStamp(
    base.Consumer[request.RequestData],
    base.Producer[timestamp.DataType]):

    def push_event(self, event: data_types.RequestData):
        data = timestamp.parse_from_dict(
            timestamp=event['timestamp'],
            path=event['timestamp'],
            source=event['source']
        )
        self._push_event(data)


def register_self():
    request_source_handler = HandleRequestToSource()
    config.subscribe(request_source_handler, request.Requests)
    config.register(request_source_handler, request_source.RequestSourceTopic)
    request_path_handler = HandleRequestToPath()
    config.subscribe(request_path_handler, request.Requests)
    config.register(request_path_handler, request_path.RequestPathTopic)
    timestamp_handler = HandleRequestToTimeStamp()
    config.subscribe(timestamp_handler,request.Requests)
    config.register(timestamp_handler,timestamp.Topic)
