class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [i for i in range(n)]  # Max cuts
        isPalindrome = [[False] * n for _ in range(n)]
        
        # Precompute palindrome substrings
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPalindrome[j + 1][i - 1]):
                    isPalindrome[j][i] = True
        
        # Compute min cuts
        for i in range(1, n):
            if isPalindrome[0][i]:
                dp[i] = 0
                continue
            for j in range(1, i + 1):
                if isPalindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
                    
        return dp[-1]