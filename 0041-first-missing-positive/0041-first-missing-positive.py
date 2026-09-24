class Solution(object):
    def firstMissingPositive(self, nums):
        nums_set = set(nums)
        
        i = 1
        while True:
            if i not in nums_set:
                return i
            i += 1
        
        