from . import handle_event
from . import handle_requests
from . import handle_rq_paths
from . import handle_rq_source
from . import handle_rq_timestamp
from .handle_event import get_producer as get_root

handle_event.register_self()
handle_requests.register_self()
handle_rq_paths.register_self()
handle_rq_source.register_self()
handle_rq_timestamp.register_self()

__all__ = [
    "get_root"
]
