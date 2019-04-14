#!/usr/bin/env python
# -*- coding:UTF-8 -*-

#
# nums = ('11', '22', '33', '44')
# nums = '_'.join(nums)
# print(nums)

# 强制转换
nums = [11, 22, 33, 44]
for i in range(0, len(nums)):
    nums[i] = str(nums[i])
li = '_'.join(nums)
print(li)
