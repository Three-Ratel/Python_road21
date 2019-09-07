def bsearch(alist, item):
    low = 0
    high = len(alist) - 1
    find = False
    while low <= high:
        mid = (low + high) // 2
        if item > alist[mid]:
            low = mid + 1
        elif item < alist[mid]:
            high = mid - 1
        else:
            find = True
            break
    return find


find = bsearch([i for i in range(1, 11)], 0)
print(find)
