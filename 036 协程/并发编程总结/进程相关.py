"""
multiprocessing包
"""

"""
1. 开启进程
"""
# import time, random, os
# from multiprocessing import Process
#
#
# def func(i):
#     time.sleep(random.random())
#     print(i, os.getpid())
#
#
# p_l = []
# for i in range(20):
#     p = Process(target=func, args=(i,))
#     p.start()
#     p_l.append(p)
#
# for p in p_l: p.join()
#
# print('main', os.getpid())


"""
2. 守护进程
"""
# import os, time
# from multiprocessing import Process
#
#
# def func(i):
#     Process(target=func, args=(1,)).start()
#     print(i, os.getpid())
#
#
# p = Process(target=func, args=(1,))
# p.daemon = True
# p.start()
# time.sleep(1)
# print('main')

"""
3. Process的其他方法
"""
# import os, time
# from multiprocessing import Process
#
# def func():
#     time.sleep(5)
#     print(os.getpid())
#
#
# p = Process(target=func)
# p.start()
# p.terminate()
# print(p.is_alive())
# time.sleep(0.1)
# print(p.is_alive())


"""
4. 面向对象开启子进程
"""
# import os, time, random
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__()
#
#     def run(self):
#         # time.sleep(random.random())
#         print(self.name, self.age, os.getpid())
#
#
# for i in range(20):
#     p = MyProcess('henry', i)
#     p.start()


"""
5. 多进程抢票系统，需要加锁
"""
# import json, time, random
# from multiprocessing import Process, Lock
#
#
# def search(i, lock):
#     with lock:
#         with open('tickets') as f:
#             dic = json.load(f)
#             print(i, '余票：', dic['count'])
#
#
# def buy(i, lcok):
#     lock.acquire()
#     with open('tickets') as f:
#         dic = json.load(f)
#     if dic['count'] > 0:
#         dic['count'] -= 1
#         print(i, '已经买到票')
#     else:
#         print(i, '没有买到票')
#     with open('tickets', mode='w') as f:
#         json.dump(dic, f)
#     lcok.release()
#
#
# lock = Lock()
# for i in range(100):
#     search(i, lock)
#     p = Process(target=buy, args=(i+1, lock))
#     p.start()


"""
6. cp模型
"""
# import requests
# from multiprocessing import Process, Queue
#
#
# def producer(url, q):
#     response = requests.get(url)
#     dic = {'url': url, 'response': response.text}
#     q.put(dic)
#
#
# def consumer(q):
#     while True:
#         dic = q.get()
#         if not dic:
#             q.put(None)
#             break
#         print(dic['url'])
#
#
# url_l = ['https://www.baidu.com', 'https://www.tencent.com', 'https://www.cnblogs.com']
# q = Queue()
# p_l = []
# if __name__ == '__main__':
#     for url in url_l:
#         p = Process(target=producer, args=(url, q))
#         p.start()
#         p_l.append(p)
#     for i in range(3):
#         Process(target=consumer, args=(q,)).start()
#     for p in p_l: p.join()
#     q.put(None)

"""
7. 生产者消费者模型之joinablequeue + daemon
"""
# import requests
# from multiprocessing import Process, JoinableQueue
#
#
# def producer(url, q):
#     response = requests.get(url)
#     dic = {'url': url, 'response': response.text}
#     q.put(dic)
#     q.join()
#
#
# def consumer(q):
#     while True:
#         dic = q.get()
#         print(dic['url'])
#         q.task_done()
#
#
# url_l = ['https://www.baidu.com', 'https://www.tencent.com', 'https://www.cnblogs.com']
# q = JoinableQueue()
# p_l = []
# if __name__ == '__main__':
#     for url in url_l:
#         p = Process(target=producer, args=(url, q))
#         p.start()
#         p_l.append(p)
#     for i in range(3):
#         c = Process(target=consumer, args=(q,))
#         c.daemon = True
#         c.start()
#     for p in p_l: p.join()

"""
8. 共享数据之manager()
"""
# from multiprocessing import Manager, Lock, Process
#
#
# def func(dic, lock):
#     with lock:
#         dic['count'] -= 1
#
#
# if __name__ == '__main__':
#     # m = Manager()
#     with Manager() as m:
#         l = Lock()
#         dic = m.dict({'count': 100})  # 共享的dict
#         p_l = []
#         for i in range(100):
#             p = Process(target=func, args=(dic, l))
#             p.start()
#             p_l.append(p)
#         for p in p_l: p.join()
#         print(dic)
