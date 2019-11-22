class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:return ''
        dict = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['k','j','l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        }
        # 回溯法，其实也是递归调用
        def backtrack(combinations,next_letter):
            if len(next_letter) == 0:
                output.append(combinations)
            else:
                for letter in dict[next_letter[0]]:
                    backtrack(combinations + letter,next_letter[1:])
        output = []
        if digits:
            backtrack("",digits)
        return output


res = []
# 添加第一个数字对应的字符
for c in dict[digits[0]]:
    res.append(c)
i = 1
while i < len(digits):
    str = dict[digits[i]]
    for c in res:
        for b in str:
            new = c + b
            res.append(new)
    i += 1
#  在函数内申请可变对象（如本题的list）并把引用传到函数外部，Python不会自行销毁！即使函数外部对象的引用计数为0后，Python也不会销毁！所以造成内存泄露！
test = Solution()
list = test.letterCombinations('23')
for item in list:
    print(item)
