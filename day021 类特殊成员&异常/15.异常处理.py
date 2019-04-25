#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
e 代表异常信息，是Exception类的对象，有一个错误信息,
即使遇到return 也会执行 finally
"""

"""
一般示例
"""
# try:
#     int('asdf')
# except ValueError as e:
#     print(e)
#
# try:
#     int('asdf')
# except IndexError as e:
#     print(e)
# except Exception as e:
#     print(e)
#
#
# def func():
#     try:
#         int('1')
#         return
#     except Exception as e:
#         print(e)
#     finally:
#         print('final')


"""
主动抛出异常
"""


# def func():
#     resutl = True
#     try:
#         with open('x.log', mode='r', encoding='utf-8') as f:
#             data = f.read()
#             if 'henry' not in data:
#                 raise Exception()
#
#     except Exception as e:
#         result = False
#     return result
#
#
# v = func()
# print(v)


"""
异常的高级用法，自定义异常
"""


# class MyException(Exception):
#     pass
#
#
# try:
#     raise MyException('haha,错了吧')
# except MyException as e:
#     print(e)


"""
示例2：高高级用法，你学不学  
"""


class MyException(Exception):
    def __init__(self, message):
        # super().__init__()
        self.message = message


try:
    raise MyException('123')
except MyException as e:
    print(e.message)



