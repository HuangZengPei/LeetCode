class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 双指针，从后往前找
        p1,p2,p = m-1,n-1,m+n-1
        while p1 >= 0 and p2 >= 0:
            #print("p1" + str(p1) + "   p2:" + str(p2))
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1 
        
        # 添加p2漏掉的
        nums1[:p2+1] = nums2[:p2+1]
<<<<<<< HEAD
        
        
        
        
=======
>>>>>>> 8e8ae7ea95c22c7fd4df80b88749e196016bf139
test = Solution()
nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n = 1

test.merge(nums1,m,nums2,n)
print(nums1)