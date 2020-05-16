class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        其余数字出现三次
        """
        ones, twos = 0, 0  # 出现一次和两次
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones

        return ones