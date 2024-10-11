#!/usr/bin/env python3

"""
101-safely_get_value
"""


from typing import TypeVar, Mapping, Union, Any


ty = TypeVar('ty')

def safely_get_value(dct: Mapping, key: Any, default: Union[ty, None]
                      = None) -> Union[ty, Any]:
    """ TypeVar """
    if key in dct:
        return dct[key]
    else:
        return default
