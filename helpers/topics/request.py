from typing import TypedDict
from ._base import base


class AbstractData(TypedDict):
    type_id: str


class RequestData(AbstractData):
    path: str
    source: str
    timestamp: str


class Requests(base.Topic[RequestData]):
    pass


Data = RequestData
Topic = Requests
