class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 先进行排序，之后双指针
        nums.sort()
        length = len(nums)
        if length < 4:return None
        res = []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i-1]:continue   #nums[i] == nums[i-1],会找到重复的组合
            for j in range(i+1, length -2):
                if j > i + 1 and nums[j] == nums[j-1]:continue
                start = j + 1
                end = length - 1
                while start < end:
                    if nums[i] + nums[j] + nums[start] + nums[end] == target:
                        res.append([nums[i],nums[j],nums[start],nums[end]])
                        start += 1
                        end -= 1
                        # 要考虑重复的部分 nums[i] == nums[i-1] or nums[j] == nums[j+1]
                        while start < end and nums[start] == nums[start-1]: start += 1
                        while start < end and nums[end] == nums[end+1]: end -= 1
                    elif nums[i] + nums[j] + nums[start] + nums[end] < target:
                        start += 1
                        while start < end and nums[start] == nums[start-1]: start += 1
                    else:
                        end -= 1
                        while start < end and nums[end] == nums[end+1]: end -= 1
        return res

test = Solution()
nums = [0,0,0,0]
target = 0
result = test.fourSum(nums,target)
print(result)
