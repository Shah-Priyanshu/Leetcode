class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}

        def dfs(i):
            # Make it till the end => 1 way
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            # If in cache => return
            if i in cache:
                return cache[i]

            res = 0
            # Current one always count, so DFS
            res += dfs(i + 1)
            # Check if can consider 2 letter
            canOne = i + 1 < len(s) and s[i] == "1"
            canTwo = i + 1 < len(s) and s[i] == "2" and s[i + 1] in "0123456"

            if canOne or canTwo:
                res += dfs(i + 2)
            cache[i] = res
            return res
        
        return dfs(0)