class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Preprocess the string to handle even-length palindromes
        processed = '#'.join('^{}$'.format(s))

        n = len(processed)
        P = [0] * n
        C, R = 0, 0

        for i in range(1, n - 1):
            mirr = 2 * C - i  # Find the mirrored position of i
            if i < R:
                P[i] = min(R - i, P[mirr])

            # Attempt to expand palindrome centered at i
            while processed[i + P[i] + 1] == processed[i - P[i] - 1]:
                P[i] += 1

            # If palindrome centered at i expands past R,
            # adjust center and right boundary
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P
        max_len, max_center = max((n, i) for i, n in enumerate(P))

        # Extract the longest palindrome substring
        start = (max_center - max_len) // 2
        return s[start:start + max_len]