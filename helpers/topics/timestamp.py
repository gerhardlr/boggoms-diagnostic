from typing import NamedTuple, TypedDict
from ._base import base


class TimestampData(TypedDict):
    path: str
    source: str


class TimestampDataTuple(NamedTuple):
    timestamp: str
    data: TimestampData


class TimestampTopic(base.Topic[TimestampDataTuple]):
    pass


Topic = TimestampTopic
DataType = TimestampDataTuple


def parse_from_dict(timestamp: str, path: str, source: str):
    return TimestampDataTuple(
        timestamp, TimestampData(
            path=path, source=source
        )
    )
