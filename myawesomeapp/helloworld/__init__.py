"""
This package's purpose is to return "Hello, world" to the caller.

It exports only the `main()` function, so that there's a clear interface
between this package's intended public function an any internal behaviors.

While anyone _could_ write this import statement without triggering a warning:

>>> from helloworld._runner import main

the leading underscore on the **module** name signals to the coder that they
shouldn't be importing the "internal" module.
"""
from ._runner import main

# This isn't required, by it makes Pylance happy that `main` is used, and is
# somewhat conventional. Read more:
# https://docs.python.org/3.9/tutorial/modules.html#importing-from-a-package
__all__ = ["main"]
