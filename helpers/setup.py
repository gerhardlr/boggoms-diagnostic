from venv import logger
from helpers import subscribers
from .base import AbstractChannel, Subscriber
from .logging_config import get_logging_config

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


def setup_channel(channel: AbstractChannel):
    for value in vars(subscribers).values():
        if isinstance(value, Subscriber):
            channel.subscribe(value)
