class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            else:
                return i
        if i == len(nums) - 1:
            return i+1

test = Solution()
nums = [1]
print(test.searchInsert(nums,0))
