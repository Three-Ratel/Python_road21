#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import random
from threading import Thread


class Singleton:
    from threading import Lock  # 复用性考虑
    __instance = None
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(random.random())  # 切换GIL锁
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


def fun():
    print(Singleton('henry', 18))


li = []
for i in range(10):
    t = Thread(target=fun)
    li.append(t)
    t.start()
for t in li: t.join()
