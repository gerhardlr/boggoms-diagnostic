import abc
from typing import Any


class Subscriber:

    @abc.abstractmethod
    def push_event(self, event: Any):
        """"""


class AbstractChannel:

    @abc.abstractmethod
    def consume(self, event):
        """"""

    @abc.abstractmethod
    def subscribe(self, subscriber: Subscriber):
        """"""


class DB:

    @abc.abstractmethod
    def push_event(self, event_name: str, event: Any):
        """"""

    @abc.abstractmethod
    def append_to_set(self, set_name, value: str):
        """"""

    @abc.abstractmethod
    def ping(self) -> Any:
        """"""

    @abc.abstractmethod
    def inc(self, key: str):
        """"""
