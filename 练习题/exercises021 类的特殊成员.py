#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
在有继承时，类中没有__init__方法，可以继承基类（不仅仅是object）
"""

# 今日作业
"""
1.列举你了解的面向对象中的特殊成员，并为每个写代码示例。
"""
# 1.__new__ __init__

# class Foo(object):
#     def __init__(self):
#         self.name = 'henry'
#
#     def __new__(cls, *args, **kwargs):
#         print('先执行这里')
#         return object.__new__(cls)
#
#
# obj = Foo()
# print(obj.name)


# 2.__str__
# class Foo(object):
#     def __str__(self):
#         return '哈哈，变身了吧'
#
#
# print(Foo())


# 3.__call__
# class Foo(object):
#     def __call__(self, *args, **kwargs):
#         print('不要总是调用我')
#
#
# Foo()()


# 4.__enter__ __exit__
# class Foo(object):
#     def __enter__(self):
#         print('进来了没')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('出去溜达溜达')
#
#     def do_what_you_want(self):
#         print('老板走了，嗨起来')
#
#
# with Foo() as f:
#     f.do_what_you_want()

# 5. __setitem__ __setitem__ __delitem__
# class Foo(object):
#     def __setitem__(self, key, value):
#         print(key, value)
#
#     def __getitem__(self, item):
#         print(item)
#
#     def __delitem__(self, key):
#         print(key)
#
#
# obj = Foo()
# obj['name'] = 'henry'
# obj['hahaha']
# del obj['name']


# 6. __dict__
# class Foo(object):
#     def __init__(self, name, age, hobby, again):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.fact = again
#
#
# obj = Foo('henry', 18, 'runing', '厉害了').__dict__
# print(obj)


# 7.__add__
# class Foo(object):
#     def __init__(self, val):
#         self.name = val
#
#     def __add__(self, other):
#         return self.name + other.name
#
#
# obj = Foo('henry')
# obj2 = Foo('haha')
# v = obj + obj2
# print(v)


"""
2.看代码写结果
"""


# class Foo(object):
#
#     def __init__(self, age):
#         self.age = age
#
#     def display(self):
#         print(self.age)
#
#
# data_list = [Foo(8), Foo(9)]
# for item in data_list:
#     print(item.age, item.display())

# 8 8 None
# 9 9 None


"""
3.看代码写结果
"""


# class Base(object):
#     def __init__(self, a1):
#         self.a1 = a1
#
#     def f2(self, arg):
#         print(self.a1, arg)
#
#
# class Foo(Base):
#     def f2(self, arg):
#         print(self.a1, '666')
#
#
# obj_list = [Base(1), Foo(2), Foo(3)]
# for obj in obj_list:
#     obj.f2(1)

# 1 1
# 666
# 666


"""
4.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print('666')
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     print(item.num)

# 1， 2， 3

"""
3.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StarkConfig):
#     pass
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)


# 1， 168
# 2， 168
# 3， 168

"""
4.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# for item in config_obj_list:
#     item.changelist(168)


# 1， 168
# 2， 168
# 666， 3


"""
5.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
# config_obj_list[1].run()
# config_obj_list[2].run()


# 2， 999
# 666， 3


"""
6.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
# print(len(site._registry))
# site.register('range', 666)
# site.register('shilei', 438)
# print(len(site._registry))
#
# site.register('lyd', StarkConfig(19))
# site.register('yjl', StarkConfig(20))
# site.register('fgz', RoleConfig(33))
# print(len(site._registry))
# print(site._registry)


# 0
# 2
# 5
# {'range': 666, 'shilei': 438, 'lyd': 对象1, 'yjl':对象2, 'fgz':对象3}

"""
7.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
# site.register('lyd', StarkConfig(19))
# site.register('yjl', StarkConfig(20))
# site.register('fgz', RoleConfig(33))
# print(len(site._registry))
#
# for k, row in site._registry.items():
#     row.changelist(5)

# 3
# 19 5
# 20 5
# 666 33

"""
8.看代码写结果
"""


# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
# site.register('lyd', StarkConfig(19))
# site.register('yjl', StarkConfig(20))
# site.register('fgz', RoleConfig(33))
# print(len(site._registry))
#
# for k, row in site._registry.items():
#     row.run()

# 3
# 19 999
# 20 999
# 666 33


"""
9.看代码写结果
"""

#
# class UserInfo(object):
#     pass
#
#
# class Department(object):
#     pass
#
#
# class StarkConfig(object):
#
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite(object):
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v(k)
#
#
# site = AdminSite()
# site.register(UserInfo, StarkConfig)
# site.register(Department, StarkConfig)
# print(len(site._registry))
# for k, row in site._registry.items():
#     row.run()


# 2
# UserInfo对象， 999
# StarkConfig对象， 999


"""
10.看代码写结果
"""


# class F3(object):
#     def f1(self):
#         ret = super().f1()
#         print(ret)
#         return 123
#
#
# class F2(object):
#     def f1(self):
#         print('123')
#
#
# class F1(F3, F2):
#     pass
#
#
# obj = F1()
# obj.f1()

# 123 None


"""
11.看代码写结果
"""


# class Base(object):
#     def __init__(self, name):
#         self.name = name
#
#
# class Foo(Base):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = "于大爷"
#
#
# obj1 = Foo('haha')
# print(obj1.name)
#
# obj2 = Base('xixi')
# print(obj2.name)


# 于大爷
# xixi

"""
12.看代码写结果
"""


# class Base(object):
#     pass
#
#
# class Foo(Base):
#     pass
#
#
# obj = Foo()
#
# print(type(obj) == Foo)
# print(type(obj) == Base)
# print(isinstance(obj, Foo))
# print(isinstance(obj, Base))

# True
# False
# True
# True


"""
13.看代码写结果
"""


# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# class RoleConfig(StarkConfig):
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# v1 = StarkConfig(1)
# v2 = RoleConfig(11)
#
# v1()
# v2()

# 1 11

"""
14.看代码写结果
"""


# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def run(self):
#         self()
#
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# class RoleConfig(StarkConfig):
#     def __call__(self, *args, **kwargs):
#         print(345)
#
#     def __getitem__(self, item):
#         return self.num[item]
#
#
# v1 = RoleConfig('alex')
# v2 = StarkConfig("wupeiqi")
#
# print(v1(1))
# print(v2(2))

# 345 None
# wupeiqi None

"""
15.补全代码
"""


# class Context:
#     def __enter__(self):
#         print('进来了')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('出去了')
#
#     def do_something(self):
#         print('哈哈，做点什么呢？')
#
#
# with Context() as ctx:
#     ctx.do_something()


"""
16.补全代码
"""

#
# class Stack(object):
#     def __init__(self):
#         self.data_list = []
#
#     def push(self, val):
#         self.data_list.append(val)
#
#     def pop(self):
#         self.data_list.pop()
#
#
# obj = Stack()
# # 调用push方法，将数据加入到data_list中。
# obj.push('alex')
# obj.push('武沛齐')
# obj.push('金老板')
#
# # 调用pop讲数据从data_list获取并删掉，注意顺序(按照后进先出的格式)
# v1 = obj.pop()  # 金老板
# v2 = obj.pop()  # 武沛齐
# v3 = obj.pop()  # alex



# 请补全Stack类中的push和pop方法，将obj的对象维护成 后进先出 的结构。


"""
17.如果主动触发一个异常？
"""
# 使用raise 关键字
# class Foo(object):
#     try:
#         raise Exception('错误了吧')
#     except Exception as e:
#         print(e)
dict

"""
18.看代码写结果
"""


# def func(arg):
#     try:
#         int(arg)
#     except Exception as e:
#         print('异常')
#     finally:
#         print('哦')
#
#
# func('123')
# func('二货')

# 哦
# 异常 哦




# ## 预习
#
# - 面向对象约束
#
#
#
#
# class BaseAuthentication(object):
#     """
#     All authentication classes should extend BaseAuthentication.
#     """
#
#     def authenticate(self, request):
#         """
#         Authenticate the request and return a two-tuple of (user, token).
#         """
#         raise NotImplementedError(".authenticate() must be overridden.")
#
#
# class Foo(BaseAuthentication):
#     def authenticate(self, request):
#         pass
#
#
# obj = Foo()
# obj.authenticate()
#
#
# - 可迭代对象
#
# - 反射
