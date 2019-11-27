class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        """
        str 回溯的每一次字符串
        list  结果集
        n  最终符合结果的字符串长度
        num   期望括号的数目
        """
        # 回溯法求解
        def backtrace(str,list,n,num):
            if len(str)==n and num ==0:
                list.append(str)
                return
            if num < 0 or (len(str) == n and num != 0):
                return
            v1 = num + 1
            v2 = num - 1
            backtrace(str + "(", list, n,v1)
            backtrace(str + ")", list, n,v2)
        result = []
        backtrace("",result,n*2,0)
        return result


# 递归求解,会漏解
result = set()
def gnenrate(str,num,result):
    if num == n:
        result.add(str+"()")
        result.add("()"+str)
        result.add("(" + str + ")")
    else:
        gnenrate(str+"()",num+1,result)
        gnenrate("()"+str,num+1,result)
        gnenrate("(" + str + ")",num+1,result)
gnenrate("",1,result)
result = list(result)
