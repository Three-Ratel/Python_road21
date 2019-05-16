#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Lock
lock = Lock()
lock.acquire()
print('-------------')
lock.acquire()
print('-------------')




