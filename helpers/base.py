import abc
from typing import Any, Generic, Type, TypeVar


T = TypeVar('T')


class Consumer(Generic[T]):

    @abc.abstractmethod
    def push_event(self, event: T):
        """"""


class Producer(Generic[T]):

    def __init__(self) -> None:
        self._subscribers: list[Consumer[T]] = []

    def subscribe(self, subscriber: Consumer[T]):
        self._subscribers.append(subscriber)

    def _push_event(self, event: T):
        for subscriber in self._subscribers:
            subscriber.push_event(event)


class Topic(Consumer[T], Producer[T]):

    def push_event(self, event: T):
        self._push_event(event)

    def register(self, producer: Producer[T]):
        producer.subscribe(self)


class BaseChannel:

    def __init__(self) -> None:
        self.topics = dict()

    def register(self, producer: Producer[T], topic_class: Type[Topic[T]]):
        if (topic := self.topics.get(topic_class)) is None:
            topic = topic_class()
            self.topics[topic_class] = topic
        topic.register(producer)

    def subscribe(self, subscriber: Consumer[T], topic_class: Type[Topic[T]]):
        if (topic := self.topics.get(topic_class)) is None:
            topic = topic_class()
            self.topics[topic_class] = topic
        topic.subscribe(subscriber)

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
