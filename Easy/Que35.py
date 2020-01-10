class Solution(object):
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     if not nums:return 0
    #     for i in range(len(nums)):
    #         if target > nums[i]:
    #             continue
    #         else:
    #             return i
    #     if i == len(nums) - 1:
    #         return i+1
            
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        二分查找
        """
        if not nums:return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = int(low + (high - low) / 2)
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return low


test = Solution()
nums = [1,3,5,6]
print(test.searchInsert(nums,7))
