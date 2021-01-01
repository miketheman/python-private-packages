"""Runner."""
from ._collector import collect
from ._combiner import combine
from ._phraser import phrasify


def main() -> str:
    """Main execution for the `helloworld` package."""
    parts = collect()
    combined = combine(parts)
    phrase = phrasify(combined)

    return phrase
