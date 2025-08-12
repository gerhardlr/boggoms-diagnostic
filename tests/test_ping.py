import abc
from typing import Generic, TypeVar
from unittest.mock import Mock

import pytest
from helpers.db import set_mock
from helpers import get_root
from helpers.data_types import Event


def test2():
    root = get_root()
    # root.push("message from producer 1")


@pytest.fixture(name='dry_run')
def fxt_dry_run() -> Mock:
    return set_mock()


@pytest.mark.usefixtures("dry_run")
def test_request_data(dry_run: Mock):
    event_data = {
        "id": "01K2531CK4XXSZPFHR6TYNTD11",
        "name": "boggoms-request",
        "data": {
                "path": "/",
                "source": "41.116.156.182",
                "timestamp": 1754665103971,
                "type_id": "RequestData"
        },
        "ts": 1754665103972
    }
    event = Event(**event_data)
    root = get_root()
    root.push(event)
    foo = dry_run
