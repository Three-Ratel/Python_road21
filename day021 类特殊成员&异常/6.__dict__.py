#!/usr/bin/env python
# -*- coding:utf-8 -*-


# class Foo(object):
#     def __init__(self, name, age, email, haha, xixi, fact):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.haha = haha
#         self.really = xixi
#         self.fact = fact
#
#
# obj = Foo('henry', 19, '123@qq.com', '多加一个', '再给你加一个', '那你厉害了')
# val = obj.__dict__                          # 去对象中找到所有变量并将其转换为字典
# print(val)



class Foo(object):
    pass



obj = Foo()
val = obj.__dict__                          # 去对象中找到所有变量并将其转换为字典
print(val)
