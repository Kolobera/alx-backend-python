#!/usr/bin/env python3
'''Task 5's module.
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of all the elements of a list"""
    return float(sum(mxd_lst))
