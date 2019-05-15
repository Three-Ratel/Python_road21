#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread


class MyThread(Thread):
    def __init__(self, i):
        self.i = i
        super().__init__()

    def run(self):
        print(self.i, self.ident)


t_l = []
for i in range(100):
    t = MyThread(i)
    t_l.append(t)
    t.start()

for t in t_l: t.join()
print('主进程结束')
