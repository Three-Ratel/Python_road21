#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
import multiprocessing

# 向queue中输入数据的函数
def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.asctime())
    queue.put(info)

# 向queue中输出数据的函数
def outputQ(queue):
    info = queue.get()
    print ('%s%s\033[32m%s\033[0m'%(str(os.getpid()), '(get):',info))

# Main
if __name__ == '__main__':
    multiprocessing.freeze_support()
    record1 = []   # store input processes
    record2 = []   # store output processes
    queue = multiprocessing.Queue(3)

    # 输入进程
    for i in range(10):
        process = multiprocessing.Process(target=inputQ,args=(queue,))
        process.start()
        record1.append(process)

    # 输出进程
    for i in range(10):
        process = multiprocessing.Process(target=outputQ,args=(queue,))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    for p in record2:
        p.join()




