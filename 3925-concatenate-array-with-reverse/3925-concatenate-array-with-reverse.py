class Solution(object):
    def concatWithReverse(self, nums):
        ans = 2 * []
        ans.extend(nums)
        ans.extend(reversed(nums))
        return ans
