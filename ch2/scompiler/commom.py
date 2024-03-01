from typing import Any, Callable, Union


def readonly_property[T](func: Callable[[T], Any]) -> property:
    class Descriptor:
        def __get__[OwnerShip](self, instance: T, owner: Union[type, OwnerShip]) -> Any:
            return func(instance)

    return property(Descriptor())
