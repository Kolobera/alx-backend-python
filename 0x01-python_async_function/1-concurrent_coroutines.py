#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns the list of all the delays (float values).
    '''
    delays = []
    for _ in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
