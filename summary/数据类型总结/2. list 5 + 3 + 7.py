#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
1. li.append(data)
任意类型数据，li操作不能直接放在print()中
"""
# li = [1, 2, 3, 4, 5, 6]
# li.append('666')
# print(li)
# li.append(['henry'])
# print(li)

"""
2. li.insert(index, data)
"""
# li = [1, 2, 3, 4, 5, 6]
# li.insert(3, 'henry')
# print(li)

"""
3. li.remove('aa')
"""
# li = ['aa', 'a', 'aacde']
# li.remove('aa')
# print(li)
# li.remove('bb')
# print(li)

"""
4. li.pop(index)
"""

li = [1, 2, 3, 4, 5, 6]
# li.pop()
# print(li)
# li.pop(3)
# print(li)
# del li[6]
# print(li)


"""
5. li.clear()
"""

# li = [1, 2, 3, 4, 5, 6]
# li.clear()
# print(li)


"""
6. li.reverse()
"""

# li = [1, 2, 3, 4, 5, 6]
# li.reverse()
# print(li)


"""
7. li.sort(reverse = True)
"""
# # reverse = True 从大到小
# # 只能是同一类型的元素
# # dict，tuple不支持排序
# li = [6, 2, 3, 1, 5, 4]
# li.sort()
# print(li)
# li = ['ba', 'ab', 'c', 'd']
# li.sort(reverse=True)
# print(li)
# li = [[6], [2, 3], [1, 5, 4]]
# li.sort()
# print(li)
#
# li = [(6, 2, 3, 1, 5, 4)]
# li.sort()
# print(li)


"""
8. li.extend(s)
"""
# # 把s中的元素，循环取出，逐个追加到list中
# # s可以是str， list， tuple， dict， set
# # dict只取keys 追加到list中
# s = 'henry'
# li = [1, 2, 3, 4, 5, 6]
# li.extend(s)
# print(li)
# s = {'a': 'e', 'b': 'c', 'c': 'h', 'd': 'o'}
# li.extend(s)
# print(li)

"""
9. len(li)
"""
# li = [1, 2, 3, 4, 5, 6]
# print(len(li))


"""
10. index
"""
# li = [1, 2, 3, 4, 5, 6]
# print(li[2])


"""
11.  切片
"""
# li = [1, 2, 3, 4, 5, 6]
# print(li[2:5])

"""
12. step
"""
# li = [1, 2, 3, 4, 5, 6]
# print(li[2::2])


"""
13. for 循环
"""
# li = [1, 2, 3, 4, 5, 6]
# for i in li:
#     print(i)

"""
14. 修改
# 使用index修改，如果只是一个值，则正常修改
# 使用index修改，如果是多个值，认为是一个tuple
# 使用切片[]修改，则循环取值加入
"""
# li = [1, 2, 3, 4, 5, 6]
# li[2] = 'henry'
# print(li)
# li[2] = 'a', 'b', 'c'
# print(li)
# li[2:3] = 'a', 'b', 'c', 0
# print(li)


"""
15. 删除del
"""
# # del 也不能放在print()里面
# li = [1, 2, 3, 4, 5, 6]
# del li[2]
# print(li)
# del li[2:]
# print()