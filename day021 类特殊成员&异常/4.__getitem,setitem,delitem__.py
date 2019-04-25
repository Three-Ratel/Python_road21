#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
用于索引操作，如字典。以上分别表示获取、设置、删除数据
"""


# class Foo(object):
#
#     def __getitem__(self, key):
#         print('get到了吧', key)
#
#     def __setitem__(self, key, value):
#         print('孤单了这么久，来这找个值', key, value)
#
#     def __delitem__(self, key):
#         print('删我干啥，你要上天', key)
#
#
# obj = Foo()
#
# result = obj['厉害了']      # 自动触发执行 __getitem__
# obj['k2'] = 'henry'        # 自动触发执行 __setitem__
# del obj['k1']              # 自动触发执行 __delitem__

obj = dict()
obj['k1'] = 123


class Foo(object):
    def __setitem__(self, key, values):
        print(key, values)

    def __getitem__(self, item):
        print(item + '666')

    def __delitem__(self, key):
        pass


obj1 = Foo()
obj1['k1'] = 123     # 内部会自动调用__setitem__方法
obj1['xxx']          # 内部会自动调用__getitem__方法
del obj1['ttt']

