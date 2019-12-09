class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        temp = [str(i+1) for i in range(n)]
        result = ""
        while len(temp) > 0:
            lTemp = len(temp)
            j = math.factorial(lTemp-1)
            t = math.ceil(k / j)-1
            k -= j*t
            result += temp[t]
            temp.pop(t)

        return result

test = Solution()
print(test.getPermutation(9,273815))
