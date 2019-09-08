alist = [22, 13, 4, 6, 8, 9, 23, 45, 76, 1]

"""冒泡排序"""


def bubble(alist):
    for j in range(len(alist) - 1):
        for i in range(1, len(alist) - j):
            if alist[i - 1] > alist[i]:
                alist[i - 1], alist[i] = alist[i], alist[i - 1]
    print(alist)


# bubble(alist)
"""选择排序"""


def select(alist):
    for j in range(len(alist) - 1, 0, -1):
        max = 0
        for i in range(j):
            if alist[max] < alist[i + 1]:
                max = i + 1
        alist[max], alist[j] = alist[j], alist[max]
    print(alist)


# select(alist)


def sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        max = 0
        for i in range(j):
            if alist[max] < alist[i + 1]:
                max = i + 1
        alist[max], alist[j] = alist[j], alist[max]
    print(alist)


def insert(alist):
    i = 1
    while i < len(alist):
        if alist[i - 1] < alist[i]:
            i += 1
        else:
            k = i
            while k > 1 and alist[k - 1] > alist[k]:
                alist[k - 1], alist[k] = alist[k], alist[k - 1]
                k -= 1
    print(alist)


# insert(alist)


# 最终代码
def sort(alist):
    gap = len(alist) // 2
    while gap >= 1:
        for i in range(gap, len(alist)):
            while i >= 1:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    print(alist)


# sort(alist)

# # 增量为gap的 shell sort
# def shell(alist):
#     gap = len(alist) // 2
#     i = gap
#     while gap:
#         while i < len(alist):
#             print(gap)
#             if alist[i - gap] < alist[i]:
#                 i += gap
#             else:
#                 # k = i
#                 # while k >= gap and alist[k - gap] > alist[k]:
#                 print(gap)
#                 alist[i - gap], alist[i] = alist[i], alist[i - gap]
#                 i -= gap
#         gap //= 2


# print(alist)
# shell(alist)
# print(alist)

"""快速排序"""


# def quick_sort(alist, left, right):
#     # 结束递归的条件
#     if left >= right:
#         return
#     low = left
#     high = right
#     base = alist[left]
#     while low < high:
#         while low < high and alist[high] > base:
#             high -= 1
#         alist[low] = alist[high]
#         while low < high and alist[low] <= base:
#             low += 1
#         alist[high] = alist[low]
#
#     alist[high] = base
#     quick_sort(alist, left, low - 1)
#     quick_sort(alist, low + 1, right)
#
#
# quick_sort(alist, 0, len(alist) - 1)
# print(alist)


def quick_sort(alist, left, right):
    if left >= right:
        return

    low = left
    high = right
    base = alist[low]
    while low < high:
        while low < high and base < alist[high]:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] <= base:
            low += 1
        alist[high] = alist[low]
    alist[low] = base
    quick_sort(alist, left, low - 1)
    quick_sort(alist, low + 1, right)


# alist = [5, 4, 3, 2, 1, 5, 3]
# quick_sort(alist, 0, len(alist) - 1)
# print(alist)

def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(1, len(li) - i):
            if li[j - 1] > li[j]:
                li[j - 1], li[j] = li[j], li[j - 1]


li = [5, 4, 3, 2, 8, 2]


# bubble_sort(li)
# print(li)


def select_sort(li):
    for j in range(len(li) - 1, 0, -1):
        max = 0
        for i in range(j+1):
            if li[max] < li[i]:
                max = i
        li[max], li[j] = li[j], li[max]
    print(li)


select_sort(li)
