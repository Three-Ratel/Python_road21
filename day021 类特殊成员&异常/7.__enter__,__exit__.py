#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
遇到关键字 with 时， __enter__ 和 __exit__ 方法要一起连用，
"""


class Foo(object):

    def __enter__(self):
        """
        进入
        :return: 返回打开的文件给 as 后的变量
        """
        self.x = open('a.txt', mode='a+', encoding='utf-8')
        return self.x

    def __exit__(self, exe_type, exc_val, exc_tb):
        """
        退出，必须有四个参数，否则报错
        :param exe_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.x.close()


with Foo() as f:
    f.write('henry'+'\n')
    f.write('echo'+'\n')




# f = open('b.txt', mode='a+', encoding='utf-8')
# f.write('hahah')

"""
重点来了
"""
# 参考并补全


class Context:

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('end')

    def do_something(self):
        print('我开始做了')


# with Context() as ctx:
#     ctx.do_something()




