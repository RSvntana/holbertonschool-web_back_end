#!/usr/bin/env python3

"""List of wait random returns"""

from typing import List
import importlib

wait_random = importlib.import_module("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Store the result in a List"""
    results = [await wait_random(max_delay) for _ in range(n)]
    return results
