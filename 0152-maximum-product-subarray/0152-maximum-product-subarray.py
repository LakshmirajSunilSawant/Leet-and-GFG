class Solution(object):
    def maxProduct(self, nums):
        curr_max = curr_min = ans = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]

            if num < 0:
                curr_max,curr_min = curr_min,curr_max


            curr_max = max(num, curr_max*num)
            curr_min = min(num, curr_min*num)

            ans = max(curr_max,ans)

        return ans


        