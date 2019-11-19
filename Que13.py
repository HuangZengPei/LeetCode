class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # python for循环里 不能改变循环变量的值
        slen = len(s)
        result = 0
        i = 0
        if not s:return 0
        while i < slen:
            if s[i] == 'I':
                result += 1
                if i != (slen -1) and s[i+1] == 'V':   # 数组越界
                    result += 3
                    i += 2
                    continue
                elif i != (slen -1) and s[i+1] == 'X':
                    result += 8
                    i += 2
                    continue
            if s[i] == 'V':
                result +=5
            if s[i] == 'X':
                result += 10
                if i != (slen -1) and s[i+1] == 'L':
                    result += 30
                    i += 2
                    continue
                elif i != (slen -1) and s[i+1] == 'C':
                    result += 80
                    i += 2
                    continue
            if s[i] == 'L':
                result += 50
            if s[i] == 'C':
                result += 100
                if i != (slen -1) and s[i+1] == 'D':
                    result += 300
                    i += 2
                    continue
                elif i != (slen -1) and s[i+1] == 'M':
                    result += 800
                    i += 2
                    continue
            if s[i] == 'D':
                result += 500
            if s[i] == 'M':
                result += 1000
            i += 1
        return result

# 使用hash表的题解
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))


test = Solution()
print(test.romanToInt('XLIV'))

