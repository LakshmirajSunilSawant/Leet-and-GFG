class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I" : 1, "V" : 5,"X":10, "L" : 50, "C" : 100, "D":500, "M":1000}
        prev_val = 0
        tot = 0
        for char in reversed(s):
            curr_val = roman_values[char]
            if curr_val >= prev_val:
                tot += curr_val
            else:
                tot -= curr_val
            prev_val = curr_val

        return tot

