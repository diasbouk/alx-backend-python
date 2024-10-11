#!/usr/bin/env python3

"""
8-make_multiplier
"""


def make_multiplier(multiplier: float) -> function:
    """ make_multiplier """
    def mult(num: float) -> float:
        """ Mult """
        return (num * multiplier)
    return mult
