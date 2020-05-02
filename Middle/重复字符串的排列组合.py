class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:return []
        res = []
        visited = []
    
        if len(S) == 1:
            return S
        for i in range(len(S)):
            if S[i] not in visited:
                visited.append(S[i])
                str = S[:i] + S[i+1:]        
                left = self.permutation(str)
                for l in left:
                    res.append(S[i] + l)
        return res
    
        
print(Solution().permutation("qeq"))