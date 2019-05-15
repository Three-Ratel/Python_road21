#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from threading import Thread


def son():
    while True:
        time.sleep(0.5)
        print('in son')


def son2():
    for i in range(5):
        time.sleep(1)


t = Thread(target=son)
t.daemon = True
t.start()

Thread(target=son2).start()
time.sleep(3)




