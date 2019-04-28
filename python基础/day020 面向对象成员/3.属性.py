#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Foo:

    @property
    def func(self):
        print(123)
        print(666)
        return '哈哈'


obj = Foo()
ret = obj.func
print(ret)




