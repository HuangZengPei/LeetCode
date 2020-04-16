class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:return []
        n = len(nums)
        nums.sort()
        
        def backtrack(current,index):
            res.append(current)
            if index == n:return

            for i in range(index,n):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(current+[nums[i]],i+1)
                
        res = []
        backtrack([],0)
        return res
        
nums = [1,2,2]
print(Solution().subsetsWithDup(nums))
        