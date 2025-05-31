# utils.py
#!/usr/bin/env python3
"""
Utility functions for nested map access, JSON fetching, and memoization.
"""

from typing import Mapping, Any, Sequence
import requests


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access a nested map using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url: str) -> dict:
    """Return the JSON content of a given URL."""
    response = requests.get(url)
    return response.json()


def memoize(fn):
    """Decorator to cache function outputs."""
    attr_name = "_{}".format(fn.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return wrapper
