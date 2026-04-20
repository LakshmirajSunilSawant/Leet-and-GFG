class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        return sum(str(n).count(str(digit)) for n in nums)