#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import requests
from multiprocessing import Process, Queue


def producer(q, url):
    response = requests.get(url)
    q.put(response.text)


def consumer(q):
    while True:
        s = q.get()
        if not s:
            q.put(None)
            break
        com = re.compile(
            '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
            '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>', re.S)
        ret = com.finditer(s)
        for i in ret:
            print({
                "id": i.group("id"),
                "title": i.group("title"),
                "rating_num": i.group("rating_num"),
                "comment_num": i.group("comment_num"),
            })


if __name__ == '__main__':
    count = 0
    q = Queue()
    p_l = []
    for i in range(10):
        count += 25
        p = Process(target=producer, args=(q, 'https://movie.douban.com/top250?start=%s&filter=' % count))
        p.start()
        p_l.append(p)
    for i in range(5):
        c = Process(target=consumer, args=(q,))
        c.start()
    for i in p_l:
        i.join()
    q.put(None)

