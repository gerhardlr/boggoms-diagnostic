from pydantic import BaseModel
from typing import Literal, Optional, TypedDict


class AbstractData(TypedDict):
    type_id: str


class RequestData(AbstractData):
    path: str
    source: str
    timestamp: str


class Event(BaseModel):
    name: str
    ts: Optional[int | None] = None
    id: Optional[str | None] = None
    data: Optional[dict] = None
    user: Optional[dict | None] = None
    v: Optional[str | None] = None
