class Solution(object):
    def minCosts(self, cost):
        ans = []
        min_cost = float('inf')

        for c in cost:
            min_cost = min(min_cost, c)
            ans.append(min_cost)

        return ans