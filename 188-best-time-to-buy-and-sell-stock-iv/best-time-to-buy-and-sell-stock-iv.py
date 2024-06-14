class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # If there are no prices, return 0
        if not prices:
            return 0

        # Get the number of days
        n = len(prices)

        # If k is large enough, treat it as unlimited transactions
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_profit += prices[i] - prices[i-1]
            return max_profit

        # Initialize the dp table with dimensions (k+1) x n
        dp = [[0] * n for _ in range(k + 1)]

        # Iterate over the number of transactions
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                # Calculate the maximum profit for i transactions up to day j
                dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
                # Update max_diff for the next day
                max_diff = max(max_diff, dp[i-1][j] - prices[j])

        # The answer is the maximum profit with at most k transactions by the last day
        return dp[k][n-1]
