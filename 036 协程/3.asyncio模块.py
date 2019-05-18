#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio


async def func():
    print(123)
    await asyncio.sleep(1)
    print(456)


loop = asyncio.get_event_loop()
loop.run_until_complete(func())
