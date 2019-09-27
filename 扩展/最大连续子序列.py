nums = [1, 2, -3, -6, 4, 5, 7]


def maxsum(nums):
    if len(nums) == 1:
        return nums[0]

    dp = res = nums[0]

    for i in range(1, len(nums)):
        dp = max(nums[i], dp + nums[i])
        res = max(dp, res)
    return res


res = maxsum(nums)
print(res)
