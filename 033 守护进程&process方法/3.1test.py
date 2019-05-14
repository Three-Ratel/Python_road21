#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from multiprocessing import Process, Lock


def view_tickets():
    with open('tickets.txt') as f:
        dic = json.load(f)
        print('还有%s张余票' % dic['count'])


def buy_tickets(user, lock):
    lock.acquire()
    with open('tickets.txt') as f:
        dic = json.load(f)
        if dic['count'] > 0:
            print('%s已买到票' % user)
            dic['count'] -= 1
        else:
            print('%s没有买到票' % user)

    with open('tickets.txt', 'w') as f:
        json.dump(dic, f)
    lock.release()


if __name__ == '__main__':
    p = Process(target=view_tickets)
    lock = Lock()
    p.start()
    for i in range(100):
        p2 = Process(target=buy_tickets, args=(i, lock))
        p2.start()
