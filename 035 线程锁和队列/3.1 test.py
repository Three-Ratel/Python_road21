#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, random
from threading import Thread


class Singleton(object):
    from threading import Lock
    __instance = None
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                time.sleep(random.random())
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def __int__(self, name, age):
        self.name = name
        self.age = age


def run():
    obj = Singleton('henry', 19)
    print(id(obj))


for i in range(20):
    t = Thread(target=run)
    t.start()
