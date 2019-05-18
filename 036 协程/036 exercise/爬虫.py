#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import gevent
from gevent.queue import Queue


def get_page(url, q):
    response = requests.get(url)
    print(type(response))
    q.put({'url': url, 'response': response.text})


def write(q):
    with open('content', 'a+', encoding='utf-8') as f:
        while True:
            dic = q.get()
            print(dic['url'])
            f.write(str(dic) + '\n')


q = Queue()
g_l = []
url_l = ['https://www.baidu.com', 'https://www.cnblogs.com/henryw/', 'https://www.cnblogs.com']
for i in url_l:
    g = gevent.spawn(get_page, i, q)
    g_l.append(g)

gevent.spawn(write, q)
gevent.joinall(g_l)
