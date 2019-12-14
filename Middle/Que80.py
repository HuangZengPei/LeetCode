class Solution:
    def removeDuplicates(self, nums):
        """
        给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。不需要考虑数组中超出新长度后面的元素。
        """
        if not nums:return 0
        curr = 1
        i = 2
        while i < len(nums):
             # 因为排好序的，所以如果nums[i] == nums[curr-1],已经重复两次了，更新i的位置
            if nums[i] == nums[curr-1]:
                    i += 1
            else:
                curr += 1
                nums[curr] = nums[i]
                i += 1
        return curr+1
        
        
test = Solution()
nums = [1,1,1,1,2,2,2,3,4,5]
print(test.removeDuplicates(nums))
print(nums)