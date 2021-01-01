"""Collector"""
from . import _hello
from . import _world


def collect() -> list[str]:
    """Collects the parts of the phrase"""
    return [_hello.main(), _world.main()]
