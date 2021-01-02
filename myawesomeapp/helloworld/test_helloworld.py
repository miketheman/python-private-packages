"""
Test helloworld.

Only test the exported public method, not the internals.

Since every bit get exercised by the publicly exported function, we get 100%
coverage without worrying about internal organization or implementations.
"""
from . import main


def test_main():
    """Tests for the main runner returns the correct string."""
    assert main() == "Hello, world."
