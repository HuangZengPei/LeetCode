class Solution:
    def uniquePaths(self, m, n) -> int:
        # 动态规划，dp[i][j]代表到达的路径总数
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
        

