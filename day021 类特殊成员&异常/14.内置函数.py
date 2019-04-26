#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
type：查看类型并判断是否属于某一个类
"""


class Foo(object):
    pass


obj = Foo()
print('obj是Foo的对象，开心吧') if type(obj) == Foo else print('哪凉快呆哪去')

"""
isinstance：又来一个查看对象的类型，晕了吧
"""


class Base(object):
    pass


class Foo(Base):
    pass


obj = Foo()
print(isinstance(obj, Foo))
print(isinstance(obj, Base))


"""
issubclass: 查看继承关系，判断是否是子类
"""


class Base(object):
    pass


class Bar(Base):
    pass


class Foo(Bar):
    pass


print(issubclass(Foo, Base))


"""
super().func(),根据 self所属类的继承关系进行查找，默认找到第一个就停止
"""


class Bar(object):
    def func(self):
        print('bar.func')
        return 123


class Base(object):

    def func(self):
        super().func()
        print('base.func')
        return 456


class Foo(Base, Bar):
    def func(self):
        v = super().func()
        print('foo.func', v)


obj = Foo()
obj.func()

