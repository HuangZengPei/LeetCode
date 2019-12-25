class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(candidates,target,0,[],result)
        return result
        
    def backtracking(self,candidates,target,start,solution,result):
        if target < 0:return
        if target == 0 :
            result.append(solution[:])
            return
        for i in range(start,len(candidates)):
            solution.append(candidates[i])
            self.backtracking(candidates,target-candidates[i],i,solution,result)
            solution.pop()
            
            


test = Solution()
candidates = [2,3,6,7]
target = 7
final = test.combinationSum(candidates,target)
print(final)
