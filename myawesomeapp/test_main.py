"""Tests for main.py"""
from myawesomeapp import main


def test_main_end_to_end():
    """Tests that the main function responds with the intended string."""
    assert main.execute() == "Hello, world."
