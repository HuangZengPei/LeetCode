class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        k = int((m+n)/2)
        if (m+n) % 2 == 1:
            return self.findKth(nums1,0,m-1,nums2,0,n-1,k+1)
        else:
            return (self.findKth(nums1, 0, m-1, nums2, 0, n-1, k) +\
                    self.findKth(nums1, 0, m-1, nums2, 0, n-1, k+1)) / 2.0
                    
    def findKth(self, nums1, l1, h1, nums2, l2, h2, k):
        m = h1 - l1 + 1
        n = h2 - l2 + 1
        
        if m > n:
            return self.findKth(nums2, l2, h2, nums1, l1, h1, k)
            
        if m == 0:
            return nums2[l2 + k - 1]
        if k == 1:
            return min(nums1[l1],nums2[l2])
            
        na = min(k/2,m)
        nb = k - na
        va = nums1[l1 + na - 1]
        vb = nums2[l2 + nb - 1]
        
        if va == vb:
            return va
        elif va < vb:
            return self.findKth(nums1,l1+na, h1, nums2, l2, l2+nb-1, k-na)
        else:
            return self.findKth(nums1,l1, l1+na-1,nums2,l2+nb, h2, k-nb)
            