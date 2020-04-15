class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)         # 小的那个数加1
        return max(dp)
        
print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))