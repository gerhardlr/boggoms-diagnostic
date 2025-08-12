from typing import Type, TypeVar
from . import base
from .channel import get_channel


_channel = None

T = TypeVar('T')


def set_channel(channel: base.BaseChannel):
    global _channel
    _channel = channel


set_channel(get_channel())


def _get_channel():
    return _channel


def register(producer: base.Producer[T], topic_class: Type[base.Topic[T]]):
    channel = _get_channel()
    assert channel
    channel.register(producer, topic_class)


def subscribe(subscriber: base.Consumer[T], topic_class: Type[base.Topic[T]]):
    channel = _get_channel()
    assert channel
    channel.subscribe(subscriber, topic_class)
