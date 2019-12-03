from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        寻找到有效的hash方法，单纯的使用ASCII码相加会有不同单词相加相同的情况
        """
        numstrdict = defaultdict(list)
        for word in strs:
             count = [0]*26
             for c in word:
                 count[ord(c)-ord('a')] += 1
             numstrdict[tuple(count)].append(word)
        return numstrdict.values()

test = Solution()
str = ["eat","tea","tan","ate","nat","bat"]
res = test.groupAnagrams(str)
print(res)
