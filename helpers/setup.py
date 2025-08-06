from .base import AbstractChannel, Subscriber
from helpers import subscribers


def setup_channel(channel: AbstractChannel):
    for value in vars(subscribers).values():
        if isinstance(value, Subscriber):
            channel.subscribe(value)
