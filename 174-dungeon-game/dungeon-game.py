class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        # Create a dp array with infinity values
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Initialize the bottom-right corner, where the princess is located
        dp[m][n - 1] = dp[m - 1][n] = 1
        
        # Fill the dp array from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(min_health_on_exit - dungeon[i][j], 1)
        
        # The minimum health needed to start at the top-left corner
        return dp[0][0]