class Solution(object):
    def alternatingSum(self, nums):
        res = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
            else:
                res -= nums[i]

        return res

        