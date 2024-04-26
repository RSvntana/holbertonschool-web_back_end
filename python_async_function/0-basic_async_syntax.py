#!/usr/bin/env python3

"""funcion to wait a period of time"""

import asyncio

import random


async def wait_random(max_delay: int = 10) -> float:
    """wait a random period of time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
