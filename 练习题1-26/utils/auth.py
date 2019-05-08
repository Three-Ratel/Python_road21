#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .myexception import MyException


class AuthMiddleware(MyException):

    def process(self, data):
        return '【auth】%s【auth】' % data
