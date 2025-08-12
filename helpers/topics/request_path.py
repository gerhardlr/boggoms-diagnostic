from typing import NamedTuple, TypedDict
from ._base import base


class RequestPathData(TypedDict):
    source: str
    timestamp: str


class RequestPathTuple(NamedTuple):
    name: str
    data: RequestPathData


class RequestPathTopic(base.Topic[RequestPathTuple]):
    pass


Topic = RequestPathTopic
Data = RequestPathTuple
