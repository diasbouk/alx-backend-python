#!/usr/bin/env python3

"""
9-element_length
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Tuple str """
    return [(i, len(i)) for i in lst]
