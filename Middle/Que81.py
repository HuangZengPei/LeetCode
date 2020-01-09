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
        while low <= high:
            middle = low + (high - low)/2
            if nums[middle] == target:
                return True
            if nums[low] == nums[middle]:
                low += 1
                continue
            elif nums[middle] == nums[high]:
                high -= 1
                continue
            if nums[low] <= nums[middle]:   # 左侧排好序递增
                if nums[low] <= target and target <= nums[middle]:
                    high = middle-1
                else:
                    low = middle+1
            else:
                if nums[middle] <= target and target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle -1
        return False
                    