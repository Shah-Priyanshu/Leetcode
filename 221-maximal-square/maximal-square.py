class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        prev = [0] * n
        curr = [0] * n
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        curr[j] = 1
                    else:
                        curr[j] = min(prev[j], curr[j-1], prev[j-1]) + 1
                    max_side = max(max_side, curr[j])
                else:
                    curr[j] = 0
            prev, curr = curr, prev
        
        return max_side * max_side
