class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base case
        if n == 0 or n == 1:
            return 1
        
        # Initialize the dp array where dp[i] stores the number of unique BSTs for i nodes
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Fill the dp array
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        
        return dp[n]