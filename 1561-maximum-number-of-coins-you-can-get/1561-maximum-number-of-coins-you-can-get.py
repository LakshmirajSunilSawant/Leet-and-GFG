class Solution(object):
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        n = len(piles) // 3
        return sum(piles[1:2*n:2])