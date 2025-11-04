class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target in nums:
                return nums.index(target)
        for i in range(n-1):
            if nums[i]< target and nums[i+1]>target:
                return i+1
        if target<nums[0]:
            return 0
        return n
