#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def run(self):
        while True:
            print(self.x, self.y, os.getpid())
            print('in myprocess')


if __name__ == '__main__':
    mp = MyProcess(1, 2)
    mp.daemon = True
    mp.start()
    time.sleep(1)
    mp.terminate()
    print(mp.is_alive())
    time.sleep(0.01)
    print(mp.is_alive())



