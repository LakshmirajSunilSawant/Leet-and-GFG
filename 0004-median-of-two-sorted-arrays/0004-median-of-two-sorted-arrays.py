class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1+nums2)
        n=len(res)
        if n%2==0:
            mid1=n//2
            mid2=mid1-1
            return (res[mid1] + res[mid2]) / 2 
        else:
            mid3=n//2

            return res[mid3]




        