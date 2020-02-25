class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        n = len(nums)
        res = -21345356
        imax = 1
        imin = 1
        for i in range(n):
            # 是负数时交换最大最小值
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(imax*nums[i], nums[i])
            imin = min(imin*nums[i], nums[i])
            res = max(res,imax)
        return res