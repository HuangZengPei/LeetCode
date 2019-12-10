class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = min(len(a),len(b))
        # 在短字符串最前方追加0
        if(len(a) < len(b)):
            a = a[::-1]
            for i in range(length,len(b)):
                a += '0'
            a = a[::-1]
        else:
            b = b[::-1]
            for i in range(length,len(a)):
                b += '0'
            b = b[::-1]
        length = len(a)-1
        ans,extra = '',0
        while length >= 0:
            extra += ord(a[length]) - ord('0')
            extra += ord(b[length]) - ord('0')
            ans += str(extra % 2)
            extra //= 2
            length -= 1
        if extra:
            ans += '1'
        return ans[::-1]



"""
优化版本
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, extra = '',0
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0:
            if i >= 0:
                extra += ord(a[i]) - ord('0')
            if j >= 0:
                extra += ord(b[j]) - ord('0')
            ans += str(extra % 2)
            extra //= 2
            i,j = i-1,j-1
        if extra == 1:
            ans += '1'
        return ans[::-1]

test = Solution()
a = '10'
b = '101'
res = test.addBinary(a,b)
print(res)
