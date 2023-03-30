#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Sequence, Tuple, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence ,int]]:
    """Returns a tuple of the lengths of the elements of a list"""
    return tuple(len(i) for i in lst)
