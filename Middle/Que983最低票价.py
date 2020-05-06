class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(days[-1] + 1)]  # 代表当前天数最少钱数
        days_index = 0
        for i in range(1,len(dp)):
            if i != days[days_index]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-1)] + costs[0],
                            dp[max(0,i-7)] + costs[1],
                            dp[max(0,i-30)] + costs[2])
                days_index += 1
        return dp[-1]