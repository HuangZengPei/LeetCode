class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        j = -1
        for i in range(lens):
            if (target - nums[i]) in nums:
                if(target - nums[i] == nums[i]) & nums.count(target-nums[i]) == 1:
                    continue
                else:
                    j = nums.index(target - nums[i],i+1)
                    break
        if j > 0:
            return [i,j]
        else:
            return []


        #通过字典 hashmap来求解
    def twoSum(self,nums,target):
        hashmap ={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target-num)
            if j is not None and i != j:
                return [i,j]
