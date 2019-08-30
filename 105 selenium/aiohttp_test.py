import asyncio

import aiohttp

# async def get_req(url):
#     print(f'获取{url}')
#     await asyncio.sleep(0.01)
#     print(f'获取{url}成功')
#     return url
#
#
# task_li = []
# count = 300
# while count < 1000:
#     start = time.time()
#     for i in range(count):
#         c = get_req(i)
#         task = asyncio.ensure_future(c)
#         task_li.append(task)
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(task_li))
#     print(count, time.time() - start)
#     count += 1

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15'
}

from aiohttp import TCPConnector
async def get_req(url):
    async with aiohttp.ClientSession(connector=TCPConnector(verify_ssl=False)) as s:
        async with await s.get(url, headers=headers) as response:
            page_text = await response.text()
            return page_text


def parse(task):
    print(task.result())


tasks = []
url_list = ['https://www.baidu.com', 'https://www.baidu.com', 'https://www.baidu.com']
for url in url_list:
    c = get_req(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
