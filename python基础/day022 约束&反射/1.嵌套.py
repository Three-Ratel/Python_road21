#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 类的嵌套


class Foo(object):
    x = 1

    def func(self):
        pass

    class Meta(object):
        y = 123
        print('hello')

        def show(self):
            print(self.y)
