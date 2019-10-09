nums = [3, 2, 4]

"""暴力解法"""


class Solution:
    def twoSum(self, nums, target=int):
        for i in range(len(nums)):
            res = target - nums[i]
            for j in range(i + 1, len(nums)):
                if res == nums[j]:
                    return [i, j]


# print(Solution().twoSum(nums, 6))

"""使用字典"""


class Solution2:
    def twoSum(self, nums, target=int):
        hashmap = {}
        for i, v in enumerate(nums):
            hashmap[v] = i
        for i, v in enumerate(nums):
            j = hashmap.get(target - v)
            if j and i != j:
                return [i, j]


# print(Solution2().twoSum(nums, 9))
"""方式三"""


class Solution3:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i


print(Solution3().twoSum(nums, 6))
