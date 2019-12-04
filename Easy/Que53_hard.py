class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        动态规划 求解子序列
        """
        if not nums:return 0
        maxEndding = nums[0]
        max = nums[0]
        for i in range(1,len(nums)):
            maxEndding = Math.max(maxEndding+nums[i],nums[i])
            max = Math.max(maxEndding,max)
        return max
