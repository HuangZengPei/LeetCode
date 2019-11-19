class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        :Description: 将字符串转换为整数
        """
        result = 0
        temp_str = ''
        num_start = False
        maxi=2147483647
        mini=-2147483648 #用于后面判断是否越界
        #去掉左边字符
        str=str.lstrip()
        if not str:return 0
        i = 0
        for c in str:
            if c >= '0' and c <= '9':
                num_start = True
                temp_str += c
            elif c == '-' and not num_start:
                temp_str += c
            elif c == '+' and not num_start:
                temp_str += c
            else:
                break
        if not temp_str:return 0
        # 只有一个+或者-号
        try:
            result = int(temp_str)
        except:
            result = 0
        result = maxi if result > maxi else mini if result < mini else result
        return result

# 正则表达式
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

test = Solution()
print(test.myAtoi('4193 with words'))
