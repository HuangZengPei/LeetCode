class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max = 0
        while i < j:
            area = min(height[i],height[j]) * (j - i)
            max = area if area >= max else max
            # 移动指针，移动高度较短的那一个
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max

test = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(test.maxArea(height))
