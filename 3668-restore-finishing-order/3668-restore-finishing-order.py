class Solution(object):
    def recoverOrder(self, order, friends):
        s = set(friends)
        res = []

        for x in order:
            if x in s:
                res.append(x)

        return res
        