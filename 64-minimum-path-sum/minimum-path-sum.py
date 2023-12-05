class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                if i > 0 and j == 0:
                    grid[i][0] += grid[i-1][0]
                if j > 0 and i == 0:
                    grid[0][j] += grid[0][j-1]
        return grid[m-1][n-1]
        