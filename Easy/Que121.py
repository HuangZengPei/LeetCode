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
        minPirce = prices[0]
        maxPro = 0
        length = len(prices)
        for i in range(1,length):
            if prices[i] < minPirce:
                minPirce = prices[i]
            elif maxPro < prices[i] - minPirce:
                maxPro = prices[i] - minPirce
        return maxPro