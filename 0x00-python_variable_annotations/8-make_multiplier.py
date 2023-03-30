#!/usr/bin/env python3
'''Task 8's module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply_by_multiplier(n: float) -> float:
        """Returns the product of n and multiplier"""
        return n * multiplier
    return multiply_by_multiplier
