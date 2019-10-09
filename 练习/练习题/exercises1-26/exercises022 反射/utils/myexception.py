#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyException(object):

        def process(self, *args):
            try:
                raise NotImplementedError('子类没有完成该功能')
            except Exception as e:
                print(e)

