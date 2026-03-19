class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1+nums2
        n.sort()
        p = len(n)
        if p%2==1:
            median = n[p//2]
        else:
            median = (n[p//2-1]+n[p//2])/2  
        return(median)