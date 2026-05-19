class Solution(object):
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7

        total = weeks * 28 + (weeks * (weeks - 1) // 2) * 7

        start = weeks + 1

        for i in range(days):
            total += start + i

        return total