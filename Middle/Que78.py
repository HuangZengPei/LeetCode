class Solution(object):
    # 求子集，动态规划
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = [[]]
        for i in range(len(nums)):
            dp = dp + [each+[nums[i]] for each in dp]
            
        return dp
        
    # 回溯法
    def backtracking(self,index,nums,k,solution,res):
        if len(solution) == k:
            res.append(solution[:])
            return
        for i in range(index,n+1):
            solution.append(i)
            self.backtracking(i+1,n,k,solution,res)
            solution.pop()