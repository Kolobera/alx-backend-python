#!/usr/bin/env python3
'''Task 6's module.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns the tuple representation of the key and value"""
    return (k, v**2)
