class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        全排列，包含重复数字
        """
        if len(nums) <= 1:  # 如果当前lst长度为1，停止递归，返回
            return [nums]
        result = []
        table = []
        for i in range(len(nums)):
            s = nums[:i]+nums[i+1:]  # 每一次拿出一个元素
            if nums[i] in table:
                continue
            else:
                table.append(nums[i])
            p = self.permuteUnique(s)  # 得到剩下元素的全排列
            for x in p:
                result.append(nums[i:i+1] + x)  # 将该元素插到剩下元素全排列的各个列表的前面
        return result


test = Solution()
data = [3,3,0,3]
res = test.permuteUnique(data)
print(res)
