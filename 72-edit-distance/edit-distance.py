class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)

        # Ensure m is the smaller of the two lengths
        if m > n:
            word1, word2, m, n = word2, word1, n, m

        # Initialize a 1D array to store the minimum operations for each column
        dp = [i for i in range(n + 1)]

        # Populate the DP array
        for i in range(1, m + 1):
            prev = dp[0]  # Store the value of the previous column
            dp[0] = i     # Update the first column

            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)

                prev = temp

        # The result is stored in the last cell of the DP array
        return dp[n]
