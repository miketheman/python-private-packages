"""
Test helloworld.

In reality, you might not actually want to test every internal method like this,
as testing the public interface is more useful than testing each individual
function, as they all get exercised.
"""
from . import _collector
from . import _combiner
from . import _runner
from . import _phraser


def test_collector():
    """Asserts that the collector collects the parts"""
    assert _collector.collect() == ["hello", "world"]


def test_combiner_combine():
    """Tests that the combiner combines with a comma-space"""
    assert _combiner.combine(["a", "b"]) == "a, b"


def test_phraser():
    """Asserts tha tthe phraser turns any set of words into a phrase"""
    assert _phraser.phrasify("hi there") == "Hi there."


def test_runner_main():
    """Tests for the main runner returns the correct string."""
    assert _runner.main() == "Hello, world."
