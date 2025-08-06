from .base import AbstractChannel, Subscriber


class Channel(AbstractChannel):

    def __init__(self):
        self._subscribers: list[Subscriber] = []
        super().__init__()

    def consume(self, event):
        for subscriber in self._subscribers:
            subscriber.push_event(event)

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)
