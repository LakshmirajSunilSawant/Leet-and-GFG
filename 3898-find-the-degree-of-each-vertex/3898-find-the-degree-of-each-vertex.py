class Solution:
    def findDegrees(self, matrix):
        n = len(matrix)
        ans = []

        for i in range(n):
            sumed = sum(matrix[i])
            ans.append(sumed)
        return ans