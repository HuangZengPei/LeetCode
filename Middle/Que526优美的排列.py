class Solution(object):
    
    def calculate(self,nums,path):
        if not nums:
            self.count += 1
        for i in range(len(nums)):
            n = len(path)
            if nums[i] % (n+1) == 0 or (n+1) % nums[i] == 0:
                new_nums = nums[:i] + nums[i+1:]
                self.calculate(new_nums,path + [nums[i]])
                
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 1:return 0
        self.count = 0
        nums = [i+1 for i in range(N)]
        self.calculate(nums,[])
        return self.count
        
        
        
print(Solution().countArrangement(2))
                
                
                
        