import numpy as np

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        one_dim = np.array(grid).flatten()
        one_set = set(one_dim)
        
        duplicate = sum(one_dim) - sum(one_set)
        n = len(one_dim)
        missing = (n * (n + 1)) // 2 - sum(one_set)
        
        return [duplicate, missing]



        