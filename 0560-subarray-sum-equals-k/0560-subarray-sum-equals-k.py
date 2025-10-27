import collections
class Solution(object):
    def subarraySum(self, arr, k):
        mp={}
        mp[0]=1
        s=0
        ans=0
        for i in arr:
            s+=i
            if(s-k in mp):
                ans+=mp[s-k]
            if(s in mp):
                mp[s]+=1
            else:
                mp[s]=1 
        return ans
