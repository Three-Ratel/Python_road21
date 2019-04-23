#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 今日作业
"""
1.简述编写类和执行类中方法的流程。
"""
# 1. 首先定义类
# 2. 实例化一个对象
# 3. 对象执行类中的操作，没有去基类中去找

"""
2.简述面向对象三大特性?
"""
# 1. 封装：对自定义函数进行分类；针对反复使用的数据进行封装，以便以后使用方便
# 2. 继承：把多个函数中公共操作单独放入一个基类中，以便其子类进行继承使用，提高代码的复用率
# 3. 多态：python不对函数参数进行限制，但使用基类中的方法时，对数据类型进行限制，即多态


"""
3.将以下函数改成类的方式并调用:
"""


# class PrintData:
#     def func(self, a1):
#         print(a1)
#
#
# v = PrintData()
# v.func('hello world')


"""
4.面向对象中的self指的是什么?
"""
# self：谁进行操作就是指谁


"""
5.以下代码体现向对象的么特点?
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


obj = Person('武沛齐', 18, '男')

# 封装，把反复使用的公共数据进行封装


"""
6.以下代码体现向对象的么特点?
"""


class Message:
    def email(self):
        """
        发送邮件
        :return:
        """
        pass

    def msg(self):
        """
        发送短信
        :return:
        """
        pass

    def wechat(self):
        """
        发送微信
        :return:
        """
        pass

# 封装：把功能类似的操作，进行归类，方便以后进行查找调用


"""
7.看代码写结果
"""


# class Foo:
#     def func(self):
#         print('foo.func')
#
#
# obj = Foo()
# result = obj.func()
# print(result)

# foo.func
# None


"""
8.定义个类，其中有计算周长和面积的方法(圆的半径通过参数传递到初始化方法)。
"""
# import math
# PI = math.pi
#
#
# class AreaPeri:
#
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         cir_peri = 2*PI*self.r
#         print('圆的周长是%s' % cir_peri)
#
#     def peri(self):
#         cir_area = PI*self.r*self.r
#         print('圆的面积是%s' % cir_area)
#
#
# v = AreaPeri(5)
# v.area()
# v.peri()

"""
9.面向对象中为什么要有继承?
"""
# 继承是为了增加函数的重用性


"""
10.Python继承时，查找成员的顺序遵循么规则?
"""
# 首先查找自己类中是否包含改成员，没有时去其基类中查找
# 有多个继承时，首先查找自己，没有再查找左边第一个类，若还没有查找，依次向后查找


"""
11.看代码写结果
"""


class Base1:
    def f1(self):
        print('base1.f1')

    def f2(self):
        print('base1.f2')

    def f3(self):
        print('base1.f3')
        self.f1()


class Base2:
    def f1(self):
        print('base2.f1')


class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()


# obj = Foo()
# obj.f0()
# foo.f0
# base1.f3
# base1.f1


"""
12.看代码写结果:
"""


class Base:
    def f1(self):
        print('base.f1')

    def f3(self):
        self.f1()
        print('base.f3')


class Foo(Base):
    def f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.f3()


# obj = Foo()
# obj.f2()
# foo.f2
# foo.f1
# base.f3

"""
13.补充代码实现
    # 需求
    1. while循环提示用户输入:用户名、密码、邮箱(正则满 邮箱格式)
    2. 为每个用户创建一个对象，并添加到list表中。
    3. 当list表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""
user_list = []


class Account:
    def __init__(self, user, pwd, email):
        self.user = user
        self.pwd = pwd
        self.email = email

    def user_add(self):
        user_list.append(self)


while True:
    if len(user_list) == 3:
        break
    user = input('请输入用户名:')
    pwd = input('请输入密码:')
    email = input('请输入邮箱:')
    v = Account(user, pwd, email)
    v.user_add()


"""
14.补充代码: 实现户注册和登录。
"""


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        while 1:
            user_name = input('please input user name(N/n): ')
            if user_name.upper() == 'N':
                return
            user_pwd = input('please input user pwd: ')
            flag = False
            for i in self.user_list:
                if user_name == i.name and user_pwd == i.pwd:
                    print("congratulations!")
                    flag = True
                    return
            if not flag:
                print('user_name or pwd is wrong')
                continue

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        while 1:
            user = input('please input your user name(N/n): ')
            if user.upper() == 'N':
                return
            for i in self.user_list:
                if user == i.name:
                    print('用户已存在，请重新输入')
                    break
            pwd = input('please input your pwd: ')
            v = User(user, pwd)
            self.user_list.append(v)
            continue

    def run(self):
        """
        主程序
        :return:
        """
        while 1:
            print("""
            1. 用户登陆
            2. 用户注册
            """)
            funcs = {'1': self.login, '2': self.register}
            choice = input('please input your choice(N/n): ')
            if choice.upper() == 'N':
                return
            if not funcs.get(choice):
                print('your choice is not exsit, please choose again.')
                continue
            funcs.get(choice)()


if __name__ == '__main__':
    obj = Account()
    obj.run()

"""
## 预习
- 类成员
http: // www.cnblogs.com / wupeiqi / p / 4493506.
html
http: // www.cnblogs.com / wupeiqi / p / 4766801.
html
"""





