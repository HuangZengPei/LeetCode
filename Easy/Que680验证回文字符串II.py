class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:return False
        low, high = 0, len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return self.isValidPalindrome(s[low+1:high+1]) or self.isValidPalindrome(s[low:high])
        return True
        
        
    
    def isValidPalindrome(self,s):
        length = len(s)
        mid = length // 2
        for i in range(mid):
            if s[i] != s[length-i-1]:
                return False
        return True
        
        
s= 'abc'
# print(s[1:3])
# print(s[0:2])
print(Solution().validPalindrome(s))