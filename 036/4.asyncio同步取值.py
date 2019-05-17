#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio


async def func():
    print(123)
    await asyncio.sleep(1)
    print(456)


loop = asyncio.get_event_loop()
t1 = loop.create_task(func())
t2 = loop.create_task(func())
task = [t1, t2]
wait_obj = asyncio.wait(task)
loop.run_until_complete(wait_obj)
for i in task:
    print(i.result())


