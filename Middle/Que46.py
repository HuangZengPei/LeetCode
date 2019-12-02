class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        全排列
        """
        if len(nums) <= 1:  # 如果当前lst长度为1，停止递归，返回
            return [nums]
        result = []
        for i in range(len(nums)):
            s = nums[:i]+nums[i+1:]  # 每一次拿出一个元素
            p = self.permute(s)  # 得到剩下元素的全排列
            for x in p:
                result.append(nums[i:i+1] + x)  # 将该元素插到剩下元素全排列的各个列表的前面
        return result


test = Solution()
data = [1,2,3]
res = test.permute(data)
print(res)
