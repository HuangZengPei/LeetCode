class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:return []
        p0,curr = 0,0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0],nums[curr] = nums[curr],nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[p2],nums[curr] = nums[curr],nums[p2]
                p2 -= 1
                # 这里交换过后，curr的值没有扫描，所以curr不能+1
            else:
                curr += 1

test = Solution()
list=[2,2,2,2,2,2,1,1,0,0,1,2]
test.sortColors(list)
print(list)
