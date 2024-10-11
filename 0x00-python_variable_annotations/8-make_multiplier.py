#!/usr/bin/env python3

"""
8-make_multiplier
"""

from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable:
    """ make_multiplier """
    return lambda x: x * multiplier
