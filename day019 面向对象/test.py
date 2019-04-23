#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Base:
    def f1(self):
        print('f1')


class Foo(Base):
    def f2(self):
        print('f2')


class Fo(Foo):
    def f3(self):
        print('f3')


obj = Fo()


obj.f1()



