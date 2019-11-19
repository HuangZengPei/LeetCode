class Solution(object):
    # 查找字符串数组中的最长公共前缀
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 找到字符数组中最短的str长度
        # 利用zip函数对字符串数组进行解压
        result = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                result += i[0]
            else:
                break
        return result



test = Solution()
str = ['abdce','abd','abdcd']
print(test.longestCommonPrefix(str))
