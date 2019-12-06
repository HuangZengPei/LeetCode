class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = len(digits)
        while n >= 1:
            plus = digits[n-1] + 1
            digits[n-1] = plus % 10
            if plus >= 10:
                n -= 1
                if n == 0:  # 考虑数字要增加一位的情况
                    l1 = [1]
                    digits = l1 + digits
            else:
                break
        return digits

test = Solution()
nums = [9]
print(test.plusOne(nums))
