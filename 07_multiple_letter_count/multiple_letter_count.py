from cmath import phase
from itertools import count
from typing import Counter


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    Counter = {}
    for list in phase:
        Counter[list] = Counter.get(list, 0) +1

    return Counter