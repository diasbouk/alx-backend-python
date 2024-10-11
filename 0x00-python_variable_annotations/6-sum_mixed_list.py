#!/usr/bin/env python3

"""
6-sum_mixed_list
"""

from typing import List


def sum_mixed_list(mxd_list: List[int | float]) -> float:
    """ Sums a mixte """
    tot: float = 0
    for i in mxd_list:
        tot += i
    return tot
