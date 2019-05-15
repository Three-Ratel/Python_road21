#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from threading import Thread, current_thread, enumerate, active_count


def func():
    print('start son thread>>>>>>>>>>>>>>>', current_thread().ident)
    time.sleep(1)
    print('end son thread', os.getpid())


t = Thread(target=func)
t.start()
print(t.ident)
print('main--------------', current_thread().ident)                   # current_ident()在哪个线程，就得到这个线程id
print(enumerate())                                                    # 统计当前进程中多少线程活着，包含主线程
print(active_count())
