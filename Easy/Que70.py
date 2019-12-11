class Solution:
    # 递归会超时
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2
        if n == 1:
            return 1
        if n<=0:
            return 0
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 转换成循环
    def climbStairs(self, n: int) -> int:
        if n==2:
            return 2
        if n == 1:
            return 1
        if n<=0:
            return 0
        s1 = 1
        s2 = 2
        num = 0
        for i in range(3,n+1):
            num = s1+ s2
            s1 = s2
            s2 = num
        return num


test = Solution()
print(test.climbStairs(38))
