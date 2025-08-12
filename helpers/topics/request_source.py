from typing import NamedTuple, TypedDict
from ._base import base


class RequestSourceData(TypedDict):
    path: str
    timestamp: str


class RequestSourceTuple(NamedTuple):
    name: str
    data: RequestSourceData


class RequestSourceTopic(base.Topic[RequestSourceTuple]):
    pass


Topic = RequestSourceTopic
DataType = RequestSourceTuple
