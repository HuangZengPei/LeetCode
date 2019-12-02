class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        positive = True
        if n < 0:
            n = -n
            positive = False
        final = 1
        while n > 0:
            if x % 2 == 0:
                x *= x
                n //= 2
            final *=x
            n -= 1
        return final if positive else 1/final


# 递归版本
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n = -n
            return 1/self.help_(x,n)
        return self.help_(x,n)

    def help_(self,x,n):
        if n==0:
            return 1
        if n%2 == 0:  #如果是偶数
            return self.help_(x*x, n//2)
        # 如果是奇数
        return self.help_(x*x,(n-1)//2)*x
