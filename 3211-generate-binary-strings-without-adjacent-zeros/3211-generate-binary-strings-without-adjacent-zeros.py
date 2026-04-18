class Solution(object):
    def validStrings(self, n):
        res = []
        
        def backtrack(path):
            if len(path) == n:
                res.append(path)
                return
            backtrack(path + "1")
            if not path or path[-1] == "1":
                backtrack(path + "0")
        
        backtrack("")
        return res