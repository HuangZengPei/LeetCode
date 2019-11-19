# Description：删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums) -> int:
        # 想法 定义两个指针
        if not nums:return 0
        i = 0
        j = 1
        while j < len(nums):
            # 当两个指针指向元素不相同时，直接修改
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

test = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(test.removeDuplicates(nums))
for i in range(len(nums)):
    print(nums[i])
