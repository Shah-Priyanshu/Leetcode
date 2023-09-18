class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Create an array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There is 1 way to reach the 1st step
        dp[2] = 2  # There are 2 ways to reach the 2nd step
        
        for i in range(3, n + 1):
            # The number of ways to reach the current step is the sum of
            # the number of ways to reach the previous two steps
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]