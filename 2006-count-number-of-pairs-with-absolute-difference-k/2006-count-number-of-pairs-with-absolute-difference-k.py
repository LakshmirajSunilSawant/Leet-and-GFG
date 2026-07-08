from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        ans = 0

        for num in nums:
            ans += freq[num + k]
            ans += freq[num-k]
            freq[num] += 1

        return ans
