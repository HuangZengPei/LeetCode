class Solution(object):
    # 暴力法
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    maxSide = max(maxSide,1)
                    # 当前可能的最大边长
                    currentMaxsize = min(rows-i, columns-j)
                    for m in range(1, currentMaxsize):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i+m][j+m] == '0':
                            flag = False
                            break
                        for n in range(m):
                            if matrix[i+m][j+n] == '0' or matrix[i+n][j+m] == '0':
                                flag = False
                                break
                        
                        if flag:
                            maxSide = max(maxSide,m+1)
                        else:
                            break
                            
        return maxSide **2
        
        
    # 动态规划法
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    maxSide = max(maxSide,dp[i][j])
        return maxSide **2
        
matrix = [["1"]]
print(Solution().maximalSquare(matrix))




                    