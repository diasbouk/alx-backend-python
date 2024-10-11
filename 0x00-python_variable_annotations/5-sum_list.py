#!/usr/bin/env python3

"""
5-sum_list
"""


def sum_list(input_list: list[float]) -> float:
    """ Sums the floats """
    total: float = 0.0
    for ele in input_list:
        total += float(ele)
    return total
