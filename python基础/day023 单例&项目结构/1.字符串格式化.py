#!/usr/bin/env python
# -*- coding:utf-8 -*-


# msg = '我是%(name)s, 年龄%(age)s' % {'name': 'alex', 'age': 19}
# print(msg)


v1 = '我是{name}, 年龄{age}'.format(name='alex', age=18)
print(v1)


v1 = '我是{name}, 年龄{age}'.format(**{'name': 'alex', 'age': 19})
print(v1)


v1 = '我是{0}, 年龄{1}'.format(*('alex', 19))
print(v1)

