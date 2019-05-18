"""
asyncio启动一个任务
"""
# import asyncio
#
#
# async def demo(i):
#     print(i)
#     await asyncio.sleep(1)
#     print(456)
#
#
# async def demo2(i):
#     print(i)
#     await asyncio.sleep(1)
#     print('haha')
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(demo(1))
# loop.run_until_complete(demo2(2))


"""
asyncio启动多个任务, 没有返回值
"""
# import asyncio
#
#
# async def demo(i):
#     print(i, 'start')
#     await asyncio.sleep(1)
#     print(i, 'end')
#
#
# loop = asyncio.get_event_loop()
# de_l = []
# for i in range(20):
#     de_l.append(demo(i))
#
#
# wait_obj = asyncio.wait(de_l)
# loop.run_until_complete(wait_obj)

"""
asyncio启动多个任务, 同步，有返回值
"""
# import asyncio, random
#
#
# async def demo(i):
#     print(i, 'start')
#     await asyncio.sleep(random.random())
#     print(i, 'end')
#     return i
#
#
# loop = asyncio.get_event_loop()
# de_l = []
# for i in range(20):
#     t = loop.create_task(demo(i))
#     de_l.append(t)
#
#
# wait_obj = asyncio.wait(de_l)
# loop.run_until_complete(wait_obj)
# for i in de_l:
#     print(i.result())


"""
asyncio启动多个任务, 异步，有返回值
"""
import asyncio, random


async def demo(i):
    print(i, 'start')
    await asyncio.sleep(random.random())
    print(i, 'end')
    return i


async def main():
    de_l = []
    for i in range(20):
        t = asyncio.ensure_future(demo(i))
        de_l.append(t)

    for ret in asyncio.as_completed(de_l):
        res = await ret
        print(res)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())






