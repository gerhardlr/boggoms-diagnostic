from typing import Protocol, Dict, Any, Optional
import abc


class VercelRequest(Protocol):
    method: str
    headers: Dict[str, str]

    def get_json(self) -> Dict[str, Any]:
        """"""

    @property
    @abc.abstractmethod
    def body(self) -> Optional[bytes]:
        """"""
