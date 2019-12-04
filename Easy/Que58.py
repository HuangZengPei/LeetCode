class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:return 0
        n = len(s)
        i = n - 1
        while i >=0:
            if s[i] == ' ':
                return len(s[i+1:n])
            else:
                i -= 1
        return len(s)

test = Solution()
print(test.lengthOfLastWord(""))
