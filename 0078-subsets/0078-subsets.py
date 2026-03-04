class Solution:
    def subsets(self, nums):
        result = []

        def build(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                build(i + 1, current)
                current.pop()

        build(0, [])
        return result
        