class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        双指针查找数组中两个相加为target的数
        """
        low = 0
        high = len(numbers) - 1
        res = []
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                res.append(low+1)
                res.append(high+1)
                return res
            elif sum < target:
                low += 1
            else:
                high -= 1
    

        
test = Solution()
numbers = [7,11,15,2]
target = 9
print(test.twoSum(numbers,target))

