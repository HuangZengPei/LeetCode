class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        n = len(nums)
        maxPos, end ,step = 0, 0, 0
        for i in range(n -1):
            if maxPos >= i:
                maxPos = max(maxPos, i+nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step