
from helpers.base import Subscriber
from helpers.db import get_db


class PingSubscriber(Subscriber):

    def push_event(self, event):
        db = get_db()
        return db.push_event("ping", event)
