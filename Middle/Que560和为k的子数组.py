class Solution(object):
    # def subarraySum(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: int
    #     超时
    #     """
    #     if not nums:return 0
    #     start , end = 0 , 0
    #     count = 0
    #     for start in range(len(nums)):
    #         sum = 0
    #         for end in range(start,len(nums)):
    #             sum += nums[end]
    #             if sum == k:
    #                 count += 1
    #             # if sum > k:
    #             #     break
    #     return count
        
    # 前缀和，hashmap存储
    def subarraySum(self, nums, k):
        """
        根据 当前前缀和，在 map 中寻找【相减 === k】的 目标前缀和。目标前缀和是一个数值，
        出现这个数值可能不止 1 次，假设为 n 次，就等价于，找到 n 个连续子数组的求和 === k，
        遍历 nums 数组，不断把 n 累加给 count，最后返回 count
        """
        d = {}
        acc = count = 0
        for num in nums:
            acc += num
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc-k]
            if acc in d:
                d[acc] += 1
            else:
                d[acc] = 1
        return d
        
        
nums = [1,2,3,3,0,3,4,2]
print(Solution().subarraySum(nums,6))
            