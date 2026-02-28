class Solution(object):
    def convertToTitle(self, colNum):
        res = ""

        while colNum > 0:
            colNum -= 1
            rem = colNum % 26
            res = chr(rem + 65) + res
            colNum //= 26

        return res