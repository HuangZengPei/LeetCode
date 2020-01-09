class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        搜索旋转排序数组，但是数组中可以有重复
        """
        if not nums:return False
        return self.binarySearch(nums,target,0,len(nums)-1)
        
    def binarySearch(self,nums, target, low, high):
        if (low >= high):
            if nums[low] == target:return True
            else:return False
        middle = low + (high - low)/2
        if nums[middle] == target:
            return True
        if nums[low] == nums[middle]:low += 1
        if nums[low] <= nums[middle]:
            if nums[low] <= target and target <= nums[middle]:    # 在左边
                return self.binarySearch(nums,target,low,middle-1)
            else:
                return self.binarySearch(nums,target,middle+1,high)
        else:
            if nums[middle] <= target and target <= nums[high]:
                return self.binarySearch(nums,target,middle+1,high)
            else:
                return self.binarySearch(nums,target,low,middle-1)