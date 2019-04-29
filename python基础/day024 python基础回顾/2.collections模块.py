#!/usr/bin/env python
# -*- coding:utf-8 -*-

info = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(info)


from collections import OrderedDict

info = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
for i, j in info.items():
    print(i, j)


from collections import namedtuple
# 可命名tuple（time 结构化时间）
# 创建了一个Course类，这个类没有方法，所有属性值不能修改
Course = namedtuple('Course', ['name',  'price', 'teacher'])
python = Course('python', 999, 'alex')

print(python)
print(python.name)
print(python.price)



