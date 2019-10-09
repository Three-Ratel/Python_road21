#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            object.__new__(cls)
        else:
            return cls.instance


obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)
print(id(obj1), id(obj2))
