"""
Main application
"""
from .helloworld import main


def execute() -> str:
    """runs main execution logic"""
    return main()


if __name__ == "__main__":  # pragma: no cover
    print(execute())
