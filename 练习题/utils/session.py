#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .myexception import MyException


class SessionMiddleware(MyException):

    def process(self, data):
        return '【session】%s【session】' % data
