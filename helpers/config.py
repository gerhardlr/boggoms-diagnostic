from .channel import Channel
from .base import AbstractChannel
from .setup import setup_channel


def get_channel() -> AbstractChannel:
    channel = Channel()
    setup_channel(channel)
    return channel
