class Solution:
    def findPermutationDifference(self, s, t) :
        pos = {ch: i for i, ch in enumerate(s)}  
        
        diff = 0
        for i, ch in enumerate(t):
            diff += abs(pos[ch] - i)
        
        return diff