class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:return 0
        if divisor ==0:return None
        posdividend = True if dividend >=0 else False
        posdivisor = True if divisor > 0 else False
        sign = posdivisor and posdividend
        res = 0
        count = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        #把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count
                dividend -= divisor
        if sign:res = -res
        return res if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1

test = Solution()
print(test.divide(1,1))
