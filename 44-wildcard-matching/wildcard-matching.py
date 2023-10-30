class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Initialize a 2D array to store matching information
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty pattern matches an empty string
        dp[0][0] = True

        # Handle patterns with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill in the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        # The result is in the bottom-right corner of the DP table
        return dp[m][n]
