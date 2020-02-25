class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0': # 基本情况，直接返回 0
            return 0
        dp = [None] * len(s) # 构建 dp 数组
        dp[0] = 1 # dp[i]表示到第i个字符的解码方法
        if len(s) > 1:
            if s[1] == '0':
                if int(s[0:2]) <= 26:
                    dp[1] = 1
                else:
                    return 0
            else:
                if int(s[0:2]) <= 26:
                    dp[1] = 2
                else:
                    dp[1] = 1
        else:
            return 1
            
        for i in range(2,len(s)):
            if s[i] == '0':
                if s[i-1] == '0':
                    return 0
                else:
                    if int(s[i-1:i+1]) <= 26:
                        dp[i] = dp[i-2]
                    else:
                        return 0
            else:
                if dp[i-1] == '0':
                    dp[i] = dp[i-1]
                else:
                    if int(s[i-1:i+1]) <= 26:
                        dp[i] = dp[i-2] + dp[i-1]
                    else:
                        dp[i] = dp[i-1]
                        
        return dp[len(s)-1]