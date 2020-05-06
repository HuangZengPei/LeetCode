class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:return False
        n = len(nums)
        maxPos, end = 0,0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, i+ nums[i])
                if i == end:
                    end = maxPos
        print(maxPos)
        return True if maxPos >= n-1 else False
        
nums = [2,3,1,1,4]
Solution().canJump(nums)