class Solution:
    def findKthBit(self, n, k):
        def solve(level, position):
            if level == 1:
                return "0"
            
            length = (1 << level) - 1
            middle = length // 2 + 1
            
            if position == middle:
                return "1"
            
            if position < middle:
                return solve(level - 1, position)
            
            mirrored_position = length - position + 1
            bit = solve(level - 1, mirrored_position)
            
            return "1" if bit == "0" else "0"
        
        return solve(n, k)