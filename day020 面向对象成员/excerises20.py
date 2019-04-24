#!/usr/bin/env python
# -*- coding:utf-8 -*-
##  作业

"""
1.简述面向对象三大特性并用代码表示。
"""


# 1.封装：


# class Foo(object):
#     def __init__(self, name, pwd):
#         self.name = name
#         self.pwd = pwd
#
#     def f(self):
#         print(123)
#
#
# obj = Foo('henry', 123)


"""
2.什么是鸭子模型？
"""
# python中类的多态又被称为鸭子模型，
# 调用类中的方法时，python解释器不会对其参数进行任何限制
# 只要参数满足类中方法内的参数操作，就可以
# 这就是鸭子模型，我们认为只要能呱呱叫的就是鸭子，只要能满足相应的参数操作就是我们想要的类型

"""
3.列举面向对象中的类成员和对象成员。
"""
# 类成员：类变量，普通/绑定方法，静态方法，类方法，属性
# 对象成员：实例变量

"""
4. @ classmethod和 @ staticmethod的区别?
"""
# @classmethod 是类方法，在定义此方法时，至少需要一个cls参数
# @staticmethod 是静态方法，在定义方法时，对参数没有限制
# 调用：类.方法名(), 对象.方法名（）

"""
5.Python中双下滑__有什么作用？
"""
# __开头（不包含名称右边的__）,表示此类变量或方法是该类私有，外部成员不能访问

"""
6.看代码写结果
"""


# class Base:
#     x = 1
#
#
# obj = Base()
# print(obj.x)
# obj.y = 123
# print(obj.y)
# obj.x = 123
# print(obj.x)
# print(Base.x)

# 1， 123， 123， 1

"""
7.看代码写结果
"""


# class Parent:
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
# Child2.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)

# 1，1，1
# 1，1，2
# 1，3，2

"""
8.看代码写结果
"""


# class Foo(object):
#     n1 = '武沛齐'
#     n2 = '金老板'
#
#     def __init__(self):
#         self.n1 = '女神'
#
#
# obj = Foo()
# print(obj.n1)
# print(obj.n2)

# '女神'
# '金老板'

"""
9.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Foo(object):
#     n1 = '武沛齐'
#
#     def __init__(self, name):
#         self.n2 = name
#
#
# obj = Foo('太白')
# print(obj.n1)
# print(obj.n2)
#
# print(Foo.n1)
# print(Foo.n2)

# 武沛齐
# 太白
# 武沛齐
# 报错


"""
10.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Foo(object):
#     a1 = 1
#     __a2 = 2
#
#     def __init__(self, num):
#         self.num = num
#         self.__salary = 1000
#
#     def show_data(self):
#         print(self.num + self.a1)
#
#
# obj = Foo(666)
#
# print(obj.num)
# print(obj.a1)
# print(obj.__salary)
# print(obj.__a2)
# print(Foo.a1)
# print(Foo.__a2)

# 666
# 1
# 报错
# 报错
# 1
# 报错


"""
11.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


class Foo(object):
    a1 = 1

    def __init__(self, num):
        self.num = num

    def show_data(self):
        print(self.num + self.a1)


# obj1 = Foo(666)
# obj1 = Foo(999)
# print(obj1.num)
# print(obj1.a1)
#
# obj1.num = 18
# obj1.a1 = 99
# print(obj1.num)
# print(obj1.a1)
#
# print(obj2.a1)
# print(obj2.num)
# print(obj2.num)
# print(Foo.a1)
# print(obj1.a1)

# 999
# 1

# 18
# 99

# 报错
# 报错
# 报错
# 1
# 99

"""
12.看代码写结果，注意返回值。
"""


# class Foo(object):
#
#     def f1(self):
#         return 999
#
#     def f2(self):
#         v = self.f1()
#         print('f2')
#         return v
#
#     def f3(self):
#         print('f3')
#         return self.f2()
#
#     def run(self):
#         result = self.f3()
#         print(result)
#
#
# obj = Foo()
# v1 = obj.run()
# print(v1)
# f3
# f2
# 999
# None

"""
13.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @staticmethod
#     def f2():
#         print('f2')
#
#
# obj = Foo()
# obj.f1()
# obj.f2()
#
# Foo.f1()
# Foo.f2()

# f1
# f2
# 少参数
# f2

"""
14.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Foo(object):
#
#     def f1(self):
#         print('f1')
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#
# obj = Foo()
# obj.f1()
# obj.f2()
#
# Foo.f1()
# Foo.f2()

# f1
# f2
# 少参数
# f2

"""
15.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Foo(object):
#
#     def f1(self):
#         print('f1')
#         self.f2()
#         self.f3()
#
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#     @staticmethod
#     def f3():
#         print('f3')
#
#
# obj = Foo()
# obj.f1()
# f1
# f2
# f3

"""
16.看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
"""


# class Base(object):
#     @classmethod
#     def f2(cls):
#         print('f2')
#
#     @staticmethod
#     def f3():
#         print('f3')
#
#
# class Foo(object):
#     def f1(self):
#         print('f1')
#         self.f2()
#         self.f3()
#
#
# obj = Foo()
# obj.f1()

# f1
# 报错
# 报错


"""
17.看代码写结果
"""


# class Foo(object):
#     def __init__(self, num):
#         self.num = num
#
#
# v1 = [Foo for i in range(10)]
# v2 = [Foo(5) for i in range(10)]
# v3 = [Foo(i) for i in range(10)]
#
# print(v1)
# print(v2)
# print(v3)

# 10个Foo类地址
# 10个Foo类对象，实例变量相同
# 10个Foo类对象，实例变量不同


"""
18.看代码写结果
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
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     print(item.num)

# 1
# 2
# 3

"""
19.看代码写结果
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
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)

# 1 666
# 2 666
# 3 666
"""
20.看代码写结果
"""


# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p3 = Person('安安', 19, d2)
#
# print(p1.name)
# print(p2.age)
# print(p3.depart)
# print(p3.depart.title)

# 武沛齐
# 18
# Department对象
# 销售部

"""
21.看代码写结果
"""


# class Department(object):
#     def __init__(self, title):
#         self.title = title
#
#
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
#
#
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message()
# p2.message()

# 我是武沛齐,年龄18,属于人事部
# 我是alex,年龄18,属于人事部


"""
22.编写类完成以下的嵌套关系
角色：学校、课程、班级
要求：
    1. 创建北京、上海、深圳三所学校。
    2. 创建课程
        北京有三种课程：Linux、Python、Go
        上海有两种课程：Linux、Python
        深圳有一种课程：Python
    3. 创建班级(班级包含：班级名称、开班时间、结课时间、班级人数)
        北京Python开设：21期、22期
        北京Linux开设：2期、3期
        北京Go开设：1期、2期
        上海Python开设：1期、2期
        上海Linux开设：2期
        深圳Python开设：1期、2期
"""


class School(object):
    def __init__(self, title):
        self.title = title


class Course(object):
    def __init__(self, course):
        self.course = course


class ClassRoom(object):
    def __init__(self, title, course, time):
        self.title = title
        self.course = course
        self.time = time

    def msg(self):
        msg = "%s%s开设：%s" % (self.title, self.course, self.time)
        print(msg)


sc1 = School('北京')
sc2 = School('上海')
sc3 = School('深圳')

co1 = Course('Python')
co2 = Course('Linux')
co3 = Course('Go')

ti1 = ClassRoom(sc1.title, co1.course, "21期、22期")
ti2 = ClassRoom(sc1.title, co2.course, "2期、3期")
ti3 = ClassRoom(sc1.title, co3.course, "1期、2期")
ti4 = ClassRoom(sc2.title, co1.course, "1期、2期")
ti5 = ClassRoom(sc2.title, co2.course, "2期")
ti6 = ClassRoom(sc3.title, co1.course, "1期、2期")


ti1.msg()
ti2.msg()
ti3.msg()
ti4.msg()
ti5.msg()
ti6.msg()






























"""
## 预习
1.对象之间的嵌套关系
2.异常处理
3.类中的特殊成员：__call__等
"""
