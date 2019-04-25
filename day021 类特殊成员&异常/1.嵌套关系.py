#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
示例3
"""


class StarkConfig(object):
    list_display = 'henry'

    def changelist(self):
        print(self.list_display)


class UserConfig(StarkConfig):
    list_display = 'echo'


class AdminSite(object):
    def __init__(self):
        self._register = {}

    def registry(self, key, arg=StarkConfig):
        self._register[key] = arg

    def run(self):
        for key, val in self._register.items():
            obj = val()
            obj.changelist()


site = AdminSite()
site.registry(1)
site.registry(2, StarkConfig)
site.registry(3, UserConfig)
site.run()



