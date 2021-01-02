"""Collector"""
from . import _words


def collect() -> list[str]:
    """Collects the parts of the phrase"""
    return [_words.hello(), _words.world()]
