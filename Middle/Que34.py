class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 寻找排序数组中目标出现的第一次和最后一次,logn
        def findfirst(self,nums,target,begin,end):
            if begin >= end:
                return -1
            index =int((begin+end)/2)
            middle = nums[index]
            if middle < target:
                return findfirst(self,nums,target,index+1,end)
            elif middle > target:
                return findfirst(self,nums,target,begin,index)
            else:
                if middle == nums[index-1]:
                    while middle == nums[index-1] and index >= 1:
                        index -=1
                    return index
                else:
                    return index

        def findlast(self,nums,target,begin,end):
            if begin>=end:
                return -1
            index =int((begin+end)/2)
            middle = nums[index]
            if middle < target:
                return findlast(self,nums,target,index+1,end)
            elif middle > target:
                return findlast(self,nums,target,begin,index)
            else:
                if middle == nums[index]:
                    while index < len(nums) -1 and middle == nums[index+1]:
                        index +=1
                        if index >= len(nums):
                            return index-1
                    return index
                else:
                    return index
        first = findfirst(self,nums,target,0,len(nums))
        last = findlast(self,nums,target,0,len(nums))
        return [first,last]

test = Solution()
nums = [5,7,7,8,8,10]
nums2 = [1]
target = 1
print(test.searchRange(nums2,target))
