"""Phraser"""


def phrasify(text) -> str:
    """Adds punctuation and capitalization"""
    punctuated = text + "."
    phrase = punctuated.capitalize()
    return phrase
