"""Tests the private `_words` package exported public functions"""

from . import hello
from . import world


def test_hello():
    """Asserts that the _hello module returns the correct string"""
    assert hello() == "hello"


def test_world():
    """Asserts that the _world module returns the correct string"""
    assert world() == "world"
