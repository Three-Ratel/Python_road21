#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def run(self):
        print(self.x + self.y, os.getpid())


if __name__ == '__main__':
    p = MyProcess(1, 2)
    p.start()
    p.join()
    print('main', os.getpid())
