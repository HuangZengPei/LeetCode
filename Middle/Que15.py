class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 先进行排序，之后双指针
        nums.sort()
        res, k = [],0
        for k in range(len(nums) - 2):
            if nums[k] > 0:break # 排过序，后面的数字肯定都大于0
            if k > 0 and nums[k] == nums[k-1]:continue   #nums[i] == nums[i-1],会找到重复的组合
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] == 0:
                    res.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    # 要考虑重复的部分 nums[i] == nums[i-1] or nums[j] == nums[j+1]
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                elif nums[k] + nums[i] + nums[j] < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return res
