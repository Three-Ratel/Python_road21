# import time
#
#
# def consumer():
#     '''任务1:接收数据,处理数据'''
#     while True:
#         x = yield
#         print(x, 'consumer')
#
#
# def producer():
#     '''任务2:生产数据'''
#     g = consumer()
#     next(g)
#     for i in range(100):
#         g.send(i)
#         print('producer')
#
#
# start = time.time()
#
# producer()
#
# stop = time.time()
# print(stop - start)

loop: int = 9
print(loop)