#!/usr/bin/env pyton3

"""
100-safe_first_element
"""


# The types of the elements of the input are not know
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
