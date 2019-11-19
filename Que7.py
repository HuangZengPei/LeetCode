class Solution(object):
    # python // 向下取整，因此正数和负数不一样
    # python 可以存储无限大的数，需要用数字判断
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        y = abs(x) if x < 0 else x
        while y > 0:
            pop = y % 10
            rev = rev * 10 + pop
            y //= 10
        if x < 0:
            rev = -rev
        if rev < -2147483648 or rev > 2147483647:
            return 0
        else:
            return rev

print(5 // 3)
print(-5 // 2)