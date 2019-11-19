class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:return ""
        if numRows == 1:return s
        # 从左向右遍历字符串，用min(numRows,len(s))个列表表示非空行
        rows = [''] * min(numRows,len(s))
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row] += c
            if cur_row == numRows - 1 or cur_row == 0:
                going_down = not going_down
            cur_row += 1 if going_down else -1
        # join,以指定字符连接序列，指定字符就是调用的字符
        result = ''.join(rows)
        return result
