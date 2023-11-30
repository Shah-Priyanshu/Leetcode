from scipy.special import comb

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Calculate the binomial coefficient C(m+n-2, n-1)
        return int(comb(m + n - 2, n - 1))