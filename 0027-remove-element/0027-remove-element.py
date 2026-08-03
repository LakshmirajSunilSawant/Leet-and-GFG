class Solution(object):
    def removeElement(self, nums, val):
        n = 0
        for num in nums:
            if num != val:
                nums[n] = num
                n += 1

        return n