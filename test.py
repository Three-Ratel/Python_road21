from multiprocessing import Manager,Queue,Process

def func(dic):
    dic['count'] -= 1

if __name__ == '__main__':
    m = Manager()
    dic = m.dict({'count': 100})
    p_l = list()
    for i in range(100):
        p = Process(target=func, args=(dic,))
        p.start()
        p_l.append(p)
    for p in p_l:p.join()
    print(dic)