class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        length = len(prices)
        buy = False
        buy_index = 0
        sold_index = 0
        for i in range(length-1):
            if prices[i] < prices[i+1] and not buy:
                buy = True
                buy_index = i
            if prices[i] > prices[i+1] and buy:
                sold_index = i
                profit += prices[sold_index] - prices[buy_index]
                buy = False
        if buy:
            profit += prices[length-1] - prices[buy_index]
        return profit
        
test = Solution()
price = [7,6,4,3,1]
print(test.maxProfit(price))             