
class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []

        candi1,candi2 = None,None
        count1,count2 = 0,0

        for num in nums:
            if num == candi1:
                count1 += 1
            elif num == candi2:
                count2 += 1
            elif count1 == 0:
                candi1,count1 = num, 1
            elif count2 == 0:
                candi2,count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        res = []
        for c in [candi1,candi2]:
            if nums.count(c) > len(nums)//3:
                res.append(c)

        return res
        

        
        
        