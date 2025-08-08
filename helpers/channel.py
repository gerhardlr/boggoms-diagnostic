from helpers.logging_config import get_logging_config
from .base import AbstractChannel, Subscriber

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


class Channel(AbstractChannel):

    def __init__(self):
        self._subscribers: list[Subscriber] = []
        super().__init__()

    def consume(self, event):
        # logger.info(f"in channel")
        for subscriber in self._subscribers:
            # logger.info(f"in channel {subscriber}")
            subscriber.push_event(event)

    def subscribe(self, subscriber: Subscriber):
        logger.info(f"in subscribe")
        self._subscribers.append(subscriber)
