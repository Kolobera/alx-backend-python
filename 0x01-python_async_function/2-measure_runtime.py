#!/usr/bin/env python3
'''Task 2's module.
'''
import asyncio
import time


wait_random = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Returns the total execution time for wait_n(n, max_delay) / n.
    '''
    start = time.perf_counter()
    asyncio.run(wait_random(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
