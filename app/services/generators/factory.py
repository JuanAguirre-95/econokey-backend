from typing import Any, Callable

from .strategies.base import BaseGenerator

generator_funcs: dict[str, Callable[..., BaseGenerator]] = {}


def get_funcs():
    return generator_funcs


def register(generator_type: str, creator_fn: Callable[..., BaseGenerator]) -> None:
    """Register a new game character type."""
    generator_funcs[generator_type] = creator_fn


def unregister(generator_type: str) -> None:
    """Unregister a game character type."""
    generator_funcs.pop(generator_type, None)


def create(arguments: dict[str, Any]) -> BaseGenerator:
    """Create a game character of a specific type, given JSON data."""
    args_copy = arguments.copy()
    print(arguments)
    generator_type = args_copy.get("generator_type")
    print(generator_type)
    try:
        creator_func = generator_funcs[generator_type]
    except KeyError:
        raise ValueError(f"Unknown generator type {generator_type!r}") from None
    return creator_func(**args_copy)
