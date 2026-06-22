class Solution(object):
    def minimumOperations(self, nums):
        sum = 0
        for i in range(len(nums)):
            if nums[i]%3 != 0:
                sum += 1

        return sum


        