class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序遍历一次
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]
        
    # 位运算，更快，无需额外空间
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
        
print(Solution().singleNumber([1,1,2,2,4]))
            