#!/usr/bin/env python3

"""
0-basic_async_syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
