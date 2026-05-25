class Solution(object):
    def subarraySum(self, nums):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
    
        total_sum = 0
    
        for i in range(n):
            start = max(0, i - nums[i])
            subarray_sum = prefix[i + 1] - prefix[start]
            total_sum += subarray_sum
    
        return total_sum