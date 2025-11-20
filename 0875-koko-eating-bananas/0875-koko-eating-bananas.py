class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        def can_finish(speed):
            hours_needed = 0
            for p in piles:
                hours_needed += (p + speed - 1)// speed

            return hours_needed <= h

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left+right) // 2


            if can_finish(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


            