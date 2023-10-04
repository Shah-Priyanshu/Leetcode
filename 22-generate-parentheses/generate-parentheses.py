class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']

        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']

        for i in range(1, n + 1):
            for j in range(i):
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        dp[i].append('(' + left + ')' + right)

        return dp[n]
