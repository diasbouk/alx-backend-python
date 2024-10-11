#!/usr/bin/env python3

"""
100-safe_first_element
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ The types of the elements of the input are not know """
    if lst:
        return lst[0]
    else:
        return None
