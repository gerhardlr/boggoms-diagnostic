
"""
R = TypeVar("R")
C = TypeVar("C", bound=AbstractData)
T = TypeVar("T", bound=Subscriber)  # Specific class type for self\
P = ParamSpec("P")


def allocate(data_cls: Type[C]) -> Callable[[Callable[[T, C], R]], Callable[[T, Event], R | None]]:
    def decorator(func: Callable[[T, C], R]) -> Callable[[T, Event], R | None]:
        @wraps(func)
        def wrapped(self: T, event: Event) -> R | None:
            if data := event.data:
                if isinstance(data, dict):
                    if type_id := data.get("type_id"):
                        data = data
                        if type_id == data_cls.__name__:
                            data = cast(C, data)
                            return func(self, data)
        return wrapped
    return decorator
"""
