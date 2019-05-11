#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
示例1
"""
# def bar():
#   def inner():
#     print(1,2,3)
#   return inner
# v = bar()
# v()


"""
示例2
"""
# name = 'henry'
# def bar():
#   name = 'echo'
#   def inner():
#     print(name)
#   return inner
# v = bar()
# v()


"""
示例3  函数会独立运行，彼此不受影响。（开辟不同的内存空间）
"""
name = '123'
def bar(name):
  def inner():
    print(name)
  return inner

v1 = bar('henry')   # {name = 'henry', inner}
v2 = bar('echo')    # {name = 'echo', inner}
v1()		# henry
v2() 		# echo
