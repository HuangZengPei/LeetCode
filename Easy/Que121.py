class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        动态规划
        """
        if len(prices) <= 1:return 0
        maxPro = 0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            maxPro = max(maxPro , prices[i]-minPrice)
            minPrice = min(minPrice , prices[i])
        return maxPro
        
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        非动态规划
        """
        minPirce = 3122314345
        maxPro = 0
        length = len(prices)
        for i in range(length):
            minPrice = min(minPirce, prices[i])
            maxPro = max(maxPro, prices[i] - minPirce)
        return maxPro