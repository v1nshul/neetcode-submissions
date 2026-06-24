class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        na = nums1 + nums2

        na.sort()

        tl = len(na)

        if tl % 2 == 0:
            return(na[tl // 2-1] + na[tl // 2])/2.0
        else:
            return na[tl // 2]        
