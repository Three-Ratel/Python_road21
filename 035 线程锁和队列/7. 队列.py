#!/usr/bin/env python
# -*- coding:utf-8 -*-
import queue
# 先进先出队列：服务
from queue import Queue

q = Queue(5)
q.put(1)
q.get()
# 后进先出队列：算法
from queue import LifoQueue

lfq = LifoQueue(4)
lfq.put(1)
lfq.put(2)
print(lfq.get())
print(lfq.get())

# 优先级队列：自动排序、vip用户、告警级别
from queue import PriorityQueue

pq = PriorityQueue()
pq.put((10, 'henry'))
pq.put((6, 'echo'))
pq.put((10, 'dean'))
print(pq.get())
print(pq.get())
print(pq.get())
