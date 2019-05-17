#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio
import random


async def func(i):
    await asyncio.sleep(random.random())
    return i


async def main():
    task_l = []
    for i in range(20):
        task = asyncio.ensure_future(func(i))
        task_l.append(task)

    for ret in asyncio.as_completed(task_l):
        ret = await ret
        print(ret)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
