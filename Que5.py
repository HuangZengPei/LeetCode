class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        result = ''
        invs = s[::-1]
        for i in range(len(s)):
            if s[i] == invs[i]:
                result += s[i]
        if result == '':
            result += s[0]
        return result