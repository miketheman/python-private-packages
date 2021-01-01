"""The combiner combines parts of the sentence"""
from typing import Iterable


def combine(parts: Iterable) -> str:
    """Takes parts and joins them all together"""
    return ", ".join(parts)
