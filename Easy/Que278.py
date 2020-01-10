# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        找到第一个错误的版本
        """
        low = 1
        high = n
        while low < high:
            middle = low + (high - low) / 2
            if isBadVersion(middle):
                high = middle -1
                if not isBadVersion(middle-1):
                    return middle
            else:
                low = middle + 1
        return low