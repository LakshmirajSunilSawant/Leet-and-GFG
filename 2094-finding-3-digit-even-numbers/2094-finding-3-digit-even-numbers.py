class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10 

        for digit in digits:
            freq[digit] += 1

        res = []

        for num in range(100, 1000,2):
            temp = freq[:]
            units = (num % 10)
            tens = (num // 10) % 10
            hundreds = (num //100)

            if (temp[hundreds] == 0):
                continue
            temp[hundreds] -= 1

            if (temp[tens] == 0):
                continue
            temp[tens] -= 1

            if (temp[units] == 0):
                continue
            temp[units] -= 1

            ans = num
            res.append(ans)

        return res

