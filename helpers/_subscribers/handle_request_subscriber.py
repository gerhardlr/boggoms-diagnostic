
from helpers.util import allocate
from helpers.base import Subscriber
from helpers.db import get_db
from helpers.data_types import Event, RequestData
from helpers.logging_config import get_logging_config

logging_config = get_logging_config()
logger = logging_config.getLogger(__name__)


class HandleRequestSubscriberPerSource(Subscriber):

    @allocate(RequestData)
    def push_event(self, event: RequestData):  # type: ignore
        db = get_db()
        db.push_event(event['source'], {
            "path": event['path'],
            "timestamp": event['timestamp']
        })
        db.push_event(event['path'], {
            "source": event['source'],
            "timestamp": event['timestamp']
        })
        db.inc(f'{event["source"]}_count')
        db.inc(f'{event["path"]}_count')
        logger.info(f"handled event for HandleRequestSubscriberPerSource")
