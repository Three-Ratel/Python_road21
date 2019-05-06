#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
send方法，会触发一次next操作，yiled结果为其返回值
"""
def func():
    print(123)
    n = yield('aaa')
    print('----->', n)
    yield 'bbb'


data = func()
next(data)
v = data.send('太厉害了，直接传进去了')
print(v)

print(dir(data))