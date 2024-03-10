class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        n = len(prices)
        leftProfit = [0] * n
        rightProfit = [0] * n
        
        # Fill leftProfit
        minPrice = prices[0]
        for i in range(1, n):
            leftProfit[i] = max(leftProfit[i-1], prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        # Fill rightProfit
        maxPrice = prices[-1]
        for i in range(n-2, -1, -1):
            rightProfit[i] = max(rightProfit[i+1], maxPrice - prices[i])
            maxPrice = max(maxPrice, prices[i])
        
        # Find the maximum sum of leftProfit and rightProfit
        maxProfit = 0
        for i in range(n):
            maxProfit = max(maxProfit, leftProfit[i] + rightProfit[i])
        
        return maxProfit

        