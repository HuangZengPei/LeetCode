class Solution(object):
    def removeElement(self, nums, val):
        """
        给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:return 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i

test = Solution()
nums = [3,3,2,3]
print(test.removeElement(nums,3))
for i in range(len(nums)):
    print(nums[i])
