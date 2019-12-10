import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pat = re.compile(r'^[\+\-]?(\d+\.\d+|\.\d+|\d+\.|\d+)(e[\+\-]?\d+)?$')  # 加上$表示以这个形式结尾
        print(re.findall(pat, s.strip()))
        return True if len(re.findall(pat, s.strip())) else False

        #return True if pattern.match(s) else False


test = Solution()
str = "1  4"
print(test.isNumber(str))
