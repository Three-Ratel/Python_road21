s = "hello {}".format('henry')

"""
43. 将list按照下列规则排序，补全代码
"""
# li = [7, -8, 5, 4, 0, -2, -5]
# print(sorted(li, key=lambda x: [x < 0, abs(x)]))

"""
50. 现有字典d={"a":26,"g":20,"e":20,"c":24,"d":23,"f":21,"b":25} 请按照字段中的value字段进行排序
"""
# d = {"a": 26, "g": 20, "e": 20, "c": 24, "d": 23, "f": 21, "b": 25}
# print(sorted(d.items(), key=lambda x: x[1]))

"""
56.从0-99这100个数中随机取出10个, 要求不能重复, 可以自己设计数据结构
"""
# import random
# li = random.sample(range(100), k=10)
# print(li)


"""
57. python 判断一个字典中是否有这些key: "AAA",'BB','C',"DD",'EEE'(不使用for while)
"""
dic = {'AAA': 1, 'BB': 2, 'CC': 3, 'DD': 4}
li = ["AAA", 'BB', 'C', "DD", 'EEE']
s1 = set(dic.keys())
s2 = set(li)
# print(s1 & s2)

"""
58. 有一个list["This","is","a","Boy","!"], 所有元素都是字符串, 对他进行大小写无关的排序
"""
li = ['This', 'is', 'a', 'boy']

li = [i.lower() for i in li]
li.sort()
# print(li)

"""
70. 用Python实现99乘法表(用两种不同的方法实现)
"""
# [print(f'{i}*{j}={i*j}', end='\t') if i != j else print(f'{i}*{j}={i*j}', '\n') for i in range(1, 10) for j in range(1, i+1)]

# for i in range(1, 10):
#     for j in range(1, i+1):
#         if j == i:
#             print(f'{i}*{j}={i*j}', '\n')
#         else:
#             print(f'{i}*{j}={i*j}', end='\t')




