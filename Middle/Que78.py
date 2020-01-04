class Solution(object):
    # 求子集，动态规划
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     dp = [[]]
    #     for i in range(len(nums)):
    #         dp = dp + [each+[nums[i]] for each in dp]
    # 
    #     return dp
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        solution = []
        self.backtracking(0,nums,solution,result)
        return result
        
    # 回溯法
    def backtracking(self,index,nums,solution,res):
        res.append(solution[:])
        for i in range(index,len(nums)):
            solution.append(nums[i])
            self.backtracking(i+1,nums,solution,res)
            print("solution" + solution)
            solution.pop()
            
test = Solution()
nums = [1,2,3]
test.subsets(nums)