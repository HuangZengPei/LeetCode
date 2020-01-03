class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(1,n,k,[],result)
        return result
        
    # 回溯法
    def backtracking(self,index,n,k,solution,res):
        if len(solution) > k:
            return
        if len(solution) == k:
            res.append(solution[:])
            return
        for i in range(index,n+1):
            solution.append(i)
            self.backtracking(i+1,n,k,solution,res)
            solution.pop()
        
    
test = Solution()
final = test.combine(4,2)
print(final)