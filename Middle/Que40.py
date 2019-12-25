class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtracking(candidates,target,0,[],result)
        return result
        
    def backtracking(self,candidates,target,start,solution,result):
        if target < 0:return
        if target == 0 :
            result.append(solution[:])
            return
        
        for i in range(start,len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            solution.append(candidates[i])
            self.backtracking(candidates,target-candidates[i],i+1,solution,result)
            solution.pop()
            
            
            
# 用时超过100%用户
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        res = []

        self.__dfs(candidates, size, 0, [], target, res)
        return res

    def __dfs(self, candidates, size, start, path, residue, res):
        if residue == 0:
            res.append(path[:])
            return

        for index in range(start, size):
            if candidates[index] > residue:
                break

            # 剪枝的前提是数组升序排序
            if index > start and candidates[index - 1] == candidates[index]:
                # [1, 1, 2, 5, 6, 7, 10]
                # 0 号索引的 1 ，从后面 6 个元素中搜索
                # 1 号索引也是 1 ，从后面 5 个元素（是上面 6 个元素的真子集）中搜索，这种情况显然上面已经包含
                continue

            path.append(candidates[index])
            # 这里要传入 index + 1，因为当前元素不能被重复使用
            # 如果 index + 1 越界，传递到下一个方法中，什么也不执行
            self.__dfs(candidates, size, index + 1, path, residue - candidates[index], res)
            path.pop()