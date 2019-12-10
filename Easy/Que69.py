class Solution:
    def mySqrt(self, x: int) -> int:
        mid = x //2
        while mid > 0:
            if mid*mid > x:
                mid //= 2
            else:
                break
        if mid*mid == x:
            return mid
        else: return mid+1

test = Solution()
print(test.mySqrt(5))
