class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        中间数和数组的第一个进行比较，[4,5,6,7,0,1,2]，>nums[0]在右边搜索
        """
        if len(nums) == 1:return nums[0]
        low = 0
        high = len(nums) - 1
        if nums[high] > nums[0]:return nums[0]   # 没有旋转
        while (low < high):
            middle = int(low + (high-low)/2)
            if nums[middle] < nums[middle - 1]:
                return nums[middle]
            if nums[middle] > nums[middle + 1]:
                return nums[middle+1]
            if nums[middle] > nums[0]:
                low = middle+1
            else:
                high = middle-1
                
                
test = Solution()
nums = [3,4,5,1,2]
print(test.findMin(nums))