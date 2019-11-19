class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        y = x
        while y > 0:
            pop = y % 10
            rev = rev * 10 + pop
            y //= 10
        if rev == x:
            return True
        else:
            return False
test = Solution()
print(test.isPalindrome(123))
print(test.isPalindrome(121))
print(test.isPalindrome(0))
print(test.isPalindrome(-123))
