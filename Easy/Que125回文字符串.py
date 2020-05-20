class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:return True
        def check(c):
            if '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z':
                return True
            return False

        s = s.lower()
        low,high = 0,len(s)-1
        while low < high:
            if not check(s[low]):
                low += 1
                continue
            if not check(s[high]):
                high -= 1
                continue
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True
        
s = "race a car"
print(Solution().isPalindrome(s))