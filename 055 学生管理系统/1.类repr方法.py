#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Studnet:
    def __init__(self, name):
        self.name = name

    # 面向用户
    def __str__(self):
        return self.name

    # 内部程序
    def __repr__(self):
        return '<{}>'.format(self.name)


class Classes:
    def __init__(self):
        # self.name = name
        self.student = []


s1 = Studnet('henry')
s2 = Studnet('echo')
print(s1)
print(s2)

c = Classes()
c.student.append(s1)
c.student.append(s2)
print(c.student)
for i in c.student:
    print(i)

