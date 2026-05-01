class Solution(object):
    def halvesAreAlike(self, s):
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        
        count = 0
        
        for i in range(mid):
            if s[i] in vowels:
                count += 1
            if s[i + mid] in vowels:
                count -= 1
        
        return count == 0