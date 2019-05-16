#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time, random
from threading import Thread, Lock


def eat1(name, lock):
    lock.acquire()
    print('%s抢到了面条' % name)
    print('%s抢到了叉子' % name)
    print('%s吃了一口面' % name)
    time.sleep(random.random())
    lock.release()


def eat2(name, lock):
    lock.acquire()
    print('%s抢到了叉子' % name)
    print('%s抢到了面条' % name)
    print('%s吃了一口面' % name)
    lock.release()


u_li = ['henry', 'echo', 'dean', 'daniel', 'diane']
lock = Lock()


Thread(target=eat1, args=(u_li[0], lock)).start()
Thread(target=eat2, args=(u_li[1], lock)).start()
Thread(target=eat1, args=(u_li[2], lock)).start()
Thread(target=eat2, args=(u_li[3], lock)).start()
Thread(target=eat1, args=(u_li[4], lock)).start()




