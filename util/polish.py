"""Functionality for conjugating words in Polish."""


def conjugate_numeric(num: int, word: str) -> str:
    """Inputs a number and base noun and returns the correctly conjugated string in Polish.

    Arguments:
        num -- the quantity, integer
        word -- the base noun, e.g. 'godzin' or 'minut'
    """
    if num == 1:
        suffix = "ę"
    else:
        last_digit: int = int(str(num)[-1])
        suffix = "y" if 1 < last_digit < 5 and num not in [12, 13, 14] else ""
    return f"{num} {word}{suffix}"
  