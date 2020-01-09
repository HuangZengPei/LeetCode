class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return binarySearch(nums,target,0,len(nums)-1)
        
    def binarySearch(nums, target, low, high):
        if (low > high):
            return -1
        middle = low + (high - low)/2
        if nums[middle] == target:
            return middle
        if nums[low] <= nums[middle]:
            if nums[low] < target and target < nums[middle]:    # 在左边
                return binarySearch(nums,target,low,middle-1)
            else:
                return binarySearch(nums,target,middle+1,high)
        else:
            if nums[middle] < target and target < nums[high]:
                return binarySearch(nums,target,middle+1,high)
            else:
                return binarySearch(nums,target,low,middle-1)
        