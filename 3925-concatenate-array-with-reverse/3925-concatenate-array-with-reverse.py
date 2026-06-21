class Solution(object):
    def concatWithReverse(self, nums):
        ans = []
        ans.extend(nums)
        ans.extend(reversed(nums))
        return ans
