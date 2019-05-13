#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from multiprocessing import Process


def send_mail(i):
    print(os.getpid())
    print('邮件已发送', i)


if __name__ == '__main__':
    li = []
    for i in range(10):
        p = Process(target=send_mail, args=(i,))
        p.start()
    li.append(p)
    for p in li: p.join()
    print(os.getpid())
    print('100封邮件已发送')
