import abc
from typing import Any


class Subscriber:

    @abc.abstractmethod
    def push_event(self, event):
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
