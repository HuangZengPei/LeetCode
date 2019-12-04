class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        暴力法
        """
        if not s: return ''
        invers = s[::-1]
        if s == invers:return s
        result = s[0] # 初始化长度为1的
        for i in range(2,len(s)+1):    # 寻找长度为2的子串
            for j in range(len(s) - i+1):
                # 取每个长度的子串，求相反，然后判断是否是回文子串

                sub = s[j:j+i]
                invs = sub[::-1]
                if sub == invs:
                    result = sub
                    break
        return result

test = Solution()
str = "abb"
res = test.longestPalindrome(str)
print(res)
