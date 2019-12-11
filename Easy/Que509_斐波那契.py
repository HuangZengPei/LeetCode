class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        f1 = 0
        f2 = 1
        for i in range(2,N+1):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn

test = Solution()
print(test.fib(3))
