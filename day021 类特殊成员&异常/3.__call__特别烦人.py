#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
对象后面加括号，触发执行。

注：构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()
"""


class Foo:
    def __call__(self, *args, **kwargs):
        print('哈哈，你变成我了吧')


Foo()()
