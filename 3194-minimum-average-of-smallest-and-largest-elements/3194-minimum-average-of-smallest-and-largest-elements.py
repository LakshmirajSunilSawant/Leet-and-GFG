class Solution:
    def minimumAverage(self, nums):
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        ans = float('inf')
        
        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            ans = min(ans, avg)
            
            left += 1
            right -= 1
        
        return ans