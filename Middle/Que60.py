class Solution(object):

    def permute(self, nums, num):
        if len(nums) <= 1:  # 如果当前lst长度为1，停止递归，返回
            return [nums]
        result = []
        count = 0
        for i in range(len(nums)):
            s = nums[:i]+nums[i+1:]  # 每一次拿出一个元素
            p = self.permute(s,num)  # 得到剩下元素的全排列
            for x in p:
                result.append(nums[i:i+1] + x)  # 将该元素插到剩下元素全排列的各个列表的前面
                count += 1
                if count == num:
                    return result
        return result

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1,n+1))
        res = self.permute(nums,k)
        ansList = res[k-1]
        ans = ""
        for c in ansList:
            ans += str(c)
        return ans

test = Solution()
print(test.getPermutation(9,273815))
