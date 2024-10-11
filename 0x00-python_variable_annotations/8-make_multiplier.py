#!/usr/bin/env python3

"""
8-make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier """
    return lambda x: x * multiplier
