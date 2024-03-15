class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        part = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        # Precompute the dp table for palindrome checking
        for right in range(n):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
        
        def dfs(i):
            if i >= n:
                res.append(part[:])
                return
            
            for j in range(i, n):
                if dp[i][j]:  # Check if s[i:j+1] is a palindrome using the dp table
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res