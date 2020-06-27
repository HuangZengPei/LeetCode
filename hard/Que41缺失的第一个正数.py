class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        排序解法
        """
        if not nums:return 1
        nums.sort()
        begin_index = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                begin_index = i
                break
        # 数组里全是负数,或者最小的正整数比1大
        if begin_index == -1 or nums[begin_index] >= 2:
            return 1
        # 从第一个正数的索引找起。当nums[i+1]和nums[i]不相邻时，直接返回nums[i] + 1
        for i in range(begin_index,len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i] + 1
        # 数组中所有正数都相邻
        return nums[len(nums)-1] + 1
        
test = Solution()
nums = [-1,-2,-10]
print(test.firstMissingPositive(nums))
