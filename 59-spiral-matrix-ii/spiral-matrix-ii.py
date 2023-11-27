class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        out = [[-1] * n for i in range(n)]

        row, col = None, None
        row_dir, col_dir = 0, 1

        for i in range(1, 1 + n * n):
            if row is None:
                row, col = 0, 0
            
            else:
                if row_dir > 0:
                    if (row + row_dir) >= n or out[row + row_dir][col] > 0:
                        row_dir, col_dir = 0, -1

                elif row_dir < 0:
                    if (row + row_dir) < 0 or out[row + row_dir][col] > 0:
                        row_dir, col_dir = 0, 1

                elif col_dir > 0:
                    if (col + col_dir) >= n or out[row][col + col_dir] > 0:
                        row_dir, col_dir = 1, 0
                
                else:
                    if (col + col_dir) < 0 or out[row][col + col_dir] > 0:
                        row_dir, col_dir = -1, 0       

                row, col = row + row_dir, col + col_dir
            

            out[row][col] = i

        return out