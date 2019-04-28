#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MyException(Exception):

    def process(self):
        raise NotImplementedError()
