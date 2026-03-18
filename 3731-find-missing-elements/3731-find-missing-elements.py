class Solution(object):
    def findMissingElements(self, nums):
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)

        result = []

        for x in range(min_val, max_val + 1):
            if x not in num_set:
                result.append(x)

        return result