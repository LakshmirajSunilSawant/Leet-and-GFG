class Solution(object):
    def maxDepth(self, s):

        stack = []
        max_depth = 0

        for char in s:
            if char == '(':
                stack.append('(')
                max_depth = max(max_depth, len(stack))
            elif char == ')':
                stack.pop()
            else:
                pass
        return max_depth


        