class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        row = [1] * n
        for i in range(1, m):
            next_row = [1] * n
            for j in range(1, n):
                next_row[j] = next_row[j-1] + row[j]
            row = next_row
        
        return row[-1]