class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:return
        ans = []
        
        def recur(pre,S):
            if not S:
                ans.append(''.join(pre))
                return
            if S[0].isalpha():
                recur(pre+[S[0].lower()],S[1:])
                recur(pre+[S[0].upper()],S[1:])
            else:
                recur(pre+[S[0]],S[1:])

        recur([],S)
        return ans



print(Solution().letterCasePermutation('zc4'))
