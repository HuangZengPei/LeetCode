class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        if len(nums) <3:return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        i = 0
        for i in range(len(nums)):
            start = i+1
            end = len(nums) -1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == target:return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    start += 1
                else:
                    end -= 1
        return result
