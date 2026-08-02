class Solution(object):
    def maxSubArray(self, nums):
        maxsum = nums[0] 
        currsum = nums[0]
        for i in nums[1:]:
            currsum = max(currsum+i, i)
            maxsum = max(currsum, maxsum)

        return maxsum
        