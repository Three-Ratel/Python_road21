#!/usr/bin/env python
# -*- coding:utf-8 -*-


## 作业

"""
1.请使用面向对象实现栈（后进先出）
"""
# li = []
# class Stack(object):
#
#     def push(self, val):
#         li.append(val)
#
#     def pop(self):
#         return li.pop()
#
#
# obj = Stack()
# obj.push('haha')
# print(li)
# obj.push('xixi')
# print(li)
# v = obj.pop()
# print(v)
# v = obj.pop()
# print(v)


"""
2.请是用面向对象实现队列（先进先出）
"""
# li = []
# class Queue(object):
#
#     def enqueue(self, val):
#         li.append(val)
#
#     def dequeue(self):
#         return li.pop(0)


"""
3.如何实现一个可迭代对象？
"""

# class Iobject(object):
#     def __iter__(self):
#         return iter([i for i in range(100)])
#
# for i in Iobject():
#     print(i)


"""
4.看代码写结果
"""

# class Foo(object):
#
#     def __init__(self):
#         self.name = '武沛齐'
#         self.age = 100
#
#
# obj = Foo()
# setattr(Foo, 'email', 'wupeiqi@xx.com')
#
# v1 = getattr(obj, 'email')
# v2 = getattr(Foo, 'email')
#
# print(v1, v2)

# wupeiqi@xx.com  wupeiqi@xx.com

"""
5.请补充代码（提：循环的列表过程中如果删除列表元素，会影响后续的循环，推荐：可以尝试从后向前找）
"""

# li = ['李杰', '女神', '金鑫', '武沛齐']
#
# name = input('请输入要删除的姓氏：')  # 如输入“李”，则删除所有姓李的人。
#

# 请补充代码
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     def del_user(self):
#         i = len(li) - 1
#         while 0 <= i:
#             if self.name in li[i]:
#                 li.pop(i)
#             i -= 1
#         print(li)
#
#
# Foo(name).del_user()

"""
6.有如下字典，请删除指定数据。
"""


# class User(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __delitem__(self, key):
#         for i in range(len(info)-1, -1, -1):
#             if info[i].name == key:
#                 info.remove(info[i])
#
#
# info = [User('武沛齐', 19), User('李杰', 73), User('李杰', 73), User('景女神', 16)]
#
# name = input('请输入要删除的用户姓名：')
# # 请补充代码将指定用户对象再info列表中删除。
# del User(1, 1)[name]
# print(info)


"""
7.补充代码实现：校园管理系统。
"""


# !/usr/bin/env python
# -*- coding:utf-8 -*-

#
# class User(object):
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#
#     def __str__(self):
#         return self.name
#
#
# class School(object):
#     """学校"""
#
#     def __init__(self):
#         # 员工字典，格式为：{"销售部": [用户对象,用户对象,] }
#         self.user_dict = {}
#
#     def invite(self, department, user_object):
#         """
#         招聘，到用户信息之后，将用户按照指定结构添加到 user_dict结构中。
#         :param department: 部门名称，字符串类型。
#         :param user_object: 用户对象，包含用户信息。
#         :return:
#         """
#         if not self.user_dict.get(department):
#             self.user_dict[department] = [user_object]
#         else:
#             self.user_dict[department].append(user_object)
#         print('添加成功')
#         for i, j in self.user_dict.items():
#             print(i, j)
#
#     def dimission(self, username, department=None):
#         """
#         离职，将用户在员工字典中移除。
#         :param username: 员工姓名
#         :param department: 部门名称，如果未指定部门名称，则遍历找到所有员工信息，并将在员工字典中移除。
#         :return:
#         """
#         if department:
#             for i, j in self.user_dict.items():
#                 if department == i:
#                     for k in j:
#                         if username == k.name:
#                             j.remove(k)
#                             print('删除成功')
#                             for i, j in self.user_dict.items():
#                                 print(i, j)
#                             return
#
#         else:
#             for l in self.user_dict.values():
#                 for m in l:
#                     if username == m.name:
#                         l.remove(m)
#                         print('删除成功')
#                         for i, j in self.user_dict.items():
#                             print(i, j)
#                         return
#
#         print('This person is not exist')
#
#     def run(self):
#         """
#         主程序
#         :return:
#         """
#
#         while 1:
#             print("""
#             1. 录入员工信息
#             2. 删除员工信息
#             """)
#             choice = input("please input your choice(N/n exit): ")
#             if choice.strip().upper() == 'N':
#                 exit()
#             if choice == '1':
#                 while 1:
#                     name = input("please input staff's name(N/n back): ")
#                     if name.strip().upper() == 'N':
#                         self.run()
#                     email = input("please input staff's email: ")
#                     age = input("please input staff's age: ")
#                     department = input("please input staff's department: ")
#
#                     """
#                     实例化用户对象
#                     """
#                     self.invite(department, User(name, email, age))
#
#             elif choice == '2':
#                 while 1:
#                     name = input("please input staff's name(N/n back): ")
#                     if name.strip().upper() == 'N':
#                         self.run()
#                     # department = input("please input staff's department: ")
#                     self.dimission(name)
#             else:
#                 print('your choice is wrong, please try again')
#                 continue
#

# if __name__ == '__main__':
#     obj = School()
#     obj.run()


"""
8.请编写网站实现如下功能。
需求：实现

1. `MIDDLEWARE_CLASSES`中的所有类，并约束每个类中必须有process方法。

2. 用户访问时，使用importlib和反射让`MIDDLEWARE_CLASSES`中的每个类对
login、logout、index方法的返回值进行包装，最终让用户看到包装后的结果。
如：用户访问: http: // 127.0.0.1: 8000 / login / ，
页面显示：    【csrf】【auth】【session】 登录 【session】 【auth】 【csrf】

用户访问: http: // 127.0.0.1: 8000 / index /  ，
页面显示：    【csrf】【auth】【session】 首页 【session】 【auth】 【csrf】

即：每个类都是对view中返回返回值的内容进行包装。
"""

MIDDLEWARE_CLASSES = [
    'utils.session.SessionMiddleware',
    'utils.auth.AuthMiddleware',
    'utils.csrf.CrsfMiddleware',
]
import importlib
from utils.myexception import MyException
print(MyException().process())
from wsgiref.simple_server import make_server

# for i in MIDDLEWARE_CLASSES:
#     path, method = i.rsplit('.', 1)
#     m_obj = importlib.import_module(path)
#     getattr(m_obj, method)()


class View(object):
    def login(self):
        return '登陆'

    def logout(self):
        return '登出'

    def index(self):
        return '首页'


def func(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    obj = View()
    # print(environ)
    method_name = environ.get('PATH_INFO').strip('/')
    if not hasattr(obj, method_name):
        return ["".encode("utf-8"), ]
    response = getattr(obj, method_name)()

    for i in MIDDLEWARE_CLASSES:
        module, method = i.rsplit('.', 1)
        module = importlib.import_module(module)
        response = getattr(module, method)().process(response)

    return [response.encode("utf-8")]


# server = make_server('127.0.0.1', 8000, func)
# server.serve_forever()


## 预习

# - 单例模式
# - logging模块
# - 项目目录结构
