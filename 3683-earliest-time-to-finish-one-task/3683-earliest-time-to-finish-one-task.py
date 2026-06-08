class Solution(object):
    def earliestTime(self, tasks):
        ans = float('inf')

        for s, t in tasks:
            ans = min(ans, s + t)

        return ans