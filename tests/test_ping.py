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


# @pytest.mark.usefixtures("dry_run")
def test_request_data(dry_run: Mock):
    event_data = {
        "id": "01K2FJFSVVBC8VHY3C85Q1HDDB",
        "name": "boggoms-request",
        "data": {
            "path": "/",
            "source": "64.23.243.66",
            "timestamp": 1755016849275,
            "type_id": "RequestData"
        },
        "ts": 1755016849275
    }
    event = Event(**event_data)
    root = get_root()
    root.push(event)
    foo = dry_run
