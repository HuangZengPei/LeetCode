class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def strtonum(self,str):
            if not str:return 0
            res = 0
            for c in str:
                append = ord(c) - ord('0')
                res = res * 10 + append
            return res
        no1 = strtonum(self,num1)
        no2 = strtonum(self,num2)
        return str(no1*no2)
