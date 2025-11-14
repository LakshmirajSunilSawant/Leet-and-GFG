class Solution(object):
    def maxOperations(self, s):
        n=len(s)
        ans=0
        c=0
        i=0
        while(i<len(s)):
            ch=s[i]
            if(ch=='1'):
                c+=1
                i+=1
            else:
                while(i<n and s[i]!='1'):
                    i+=1
                ans+=c
        return ans
        