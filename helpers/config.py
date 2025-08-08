from .channel import Channel
from .base import AbstractChannel
from .setup import setup_channel
from .logging_config import get_logging_config


logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


def get_channel() -> AbstractChannel:
    channel = Channel()
    logger.info("setting up channel")
    setup_channel(channel)
    return channel
