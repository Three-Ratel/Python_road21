#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import json
from multiprocessing import Process, Lock


def search_ticket(user):
    with open('tickets.txt') as f:
        dic = json.load(f)
        print('%s查询结果：%s张余票' %(user, dic['count']))


def buy_ticket(user, lock):
    # with lock:
    lock.acquire()
    with open('tickets.txt') as f:
        dic = json.load(f)
    if dic["count"] > 0:
        print('%s已买到票' % user)
        dic["count"] -= 1
    else:
        print('%s没买到票' % user)
    with open('tickets.txt', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(40):
        search_ticket('user%s ' % (i + 1), )
        p = Process(target=buy_ticket, args=('user%s '%(i+1), lock))
        p.start()
