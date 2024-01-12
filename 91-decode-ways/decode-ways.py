class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        prev, curr = 1, 1

        for i in range(1, len(s)):
            if s[i] == '0':
                curr = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and '0' <= s[i] <= '6'):
                curr, prev = curr + prev, curr
            else:
                prev = curr

        return curr