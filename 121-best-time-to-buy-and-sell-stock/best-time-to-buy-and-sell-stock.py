class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Initialize min_price to infinity
        max_profit = 0  # Initialize max_profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update min_price if current price is lower
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max_profit if current profit is higher
                
        return max_profit