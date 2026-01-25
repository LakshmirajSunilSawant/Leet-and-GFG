class Solution(object):
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0

        ans = float('inf')
        nums.sort()

        for i in range(len(nums)- k + 1):
            ans = min(ans, nums[i + k - 1]-nums[i])

        return ans
        
        