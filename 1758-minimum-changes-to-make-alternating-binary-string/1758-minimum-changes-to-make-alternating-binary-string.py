class Solution:
    def minOperations(self, s):
        start_with_zero = 0
        start_with_one = 0

        for i, ch in enumerate(s):
            if i % 2 == 0:
                if ch != '0':
                    start_with_zero += 1
                if ch != '1':
                    start_with_one += 1
            else:
                if ch != '1':
                    start_with_zero += 1
                if ch != '0':
                    start_with_one += 1

        return min(start_with_zero, start_with_one)        