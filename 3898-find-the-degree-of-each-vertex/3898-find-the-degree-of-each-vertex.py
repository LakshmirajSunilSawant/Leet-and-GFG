class Solution:
    def findDegree(self, matrix):
        n = len(matrix)
        ans = []

        for i in range(n):
            degree = sum(matrix[i])
            ans.append(degree)

        return ans