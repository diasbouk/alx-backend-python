#!/usr/bin/env python3
from typing import List

"""
5-sum_list
"""


def sum_list(input_list: List[float]) -> float:
    """ Sums the floats """
    total: float = 0
    for ele in input_list:
        total += ele
    return total
