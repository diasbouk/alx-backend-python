#!/usr/bin/env python3

"""
7-to_kv.py
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """ Returns a tuple with k, (v)2"""
    return (k, v * v)
