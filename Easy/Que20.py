class Solution:
    # 使用栈完成括号的匹配
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')','[':']','{':'}'}
        if not s:return True
        # 判断长度是不是奇数，奇数直接False
        if len(str) % 2 != 0: return False
        for c in s:
            if c in dic:
                stack.append(c)
            # 不是奇数，不为0，则有括号，但是stack为空，则以右括号开始，返回False
            elif len(stack) == 0: return False
            elif dic.get(stack.pop()) != c:return False
        if len(stack) == 0:
            return True
        else:
            return False

test = Solution()
str = '()'
print(test.isValid(str))
