class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:return []
    
        def judge(str):
            str2 = str[::-1]
            return True if str == str2 else False
    
        def backtrack(current,index):
            if index == len(s):
                result.append(current)
                return
            for i in range(index+1,len(s)+1):
                temp_str = s[index:i]
                if judge(temp_str):
                    backtrack(current + [temp_str],i)
    
        result = []
        current = []
        backtrack(current,0)
        return result
    

test = Solution()
print(test.partition("aab"))