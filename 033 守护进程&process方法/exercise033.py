#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
0. 整理两天的笔记和每一个课上例题
1、进程间内存是否共享？如何实现通讯？
2、请聊聊进程队列的特点和实现原理？
3、请画出进程的三状态转换图
4、从你的角度说说进程在计算机中扮演什么角色？
5、使用进程实现并发的socket的server端
"""
"""
1. 进程间内存不共享， IPC（inter-Process communication），基于socket（文件家族）， pickle 和 Lock
"""

"""
2. 进程队列
    1. 先进先出
    2. 基于socket，pickle，Lock
    3. 数据安全
"""

"""
3. 
"""

"""
4. 进程是计算中运行的程序，是资源分配最小单位，为我们完成一些列指定的操作，实现某些功能
"""

"""
5、使用进程实现并发的socket的server端
"""
from multiprocessing import Process
from socket import socket, SOL_SOCKET, SO_REUSEADDR


def chat(con):
    while True:
        msg = con.recv(1024).decode('utf-8')
        con.send(msg.upper().encode('utf-8'))


if __name__ == '__main__':
    sk = socket()
    sk.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sk.bind(('127.0.0.1', 9000))
    sk.listen()
    while True:
        con, addr = sk.accept()
        p = Process(target=chat, args=(con,))
        p.start()
