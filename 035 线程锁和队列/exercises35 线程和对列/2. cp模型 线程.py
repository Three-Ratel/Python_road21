#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests, re
from queue import Queue
from datetime import datetime
from threading import Thread


def producer(q, url):
    content = requests.get(url)
    dic = {'url': url, 'content': content.text}
    q.put(dic)


def consumer(q):
    while True:
        dic = q.get()
        if not dic:
            q.put(None)
            break
        file_name = re.findall('www\.(.*)\.com', dic['url'])[0]
        str_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        file_name = str_time + file_name
        with open(file_name, mode='w', encoding='utf-8') as f:
            f.write(dic['content'])
        print(dic['url'])


p_l = []
q = Queue()
url_l = ['https://www.baidu.com', 'https://www.meijutt.com/alltop_hit.html', 'https://www.cnblogs.com/henryw/',
         'https://www.cnblogs.com']

for i in range(len(url_l)):
    p = Thread(target=producer, args=(q, url_l[i]))
    p.start()
    p_l.append(p)
for i in range(2):
    Thread(target=consumer, args=(q,)).start()
for p in p_l: p.join()
q.put(None)
