class Solution(object):
    # 暴力法，另外还有KMP算法等，继续学习
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:return 0
        # needle 的长度更大
        if len(needle) > len(haystack): return -1
        begin = needle[0]
        length = len(needle)
        i = 0
        while i < len(haystack):
            # 首字母相同，开始比较
            if begin == haystack[i]:
                part = haystack[i:i+length]
                if part == needle:
                    return i
                else:
                    i += 1
            else:
                i += 1
        if i == len(haystack):
            return -1

test = Solution()
haystack = "hello"
needle = "ll"
print(test.strStr(haystack,needle))
