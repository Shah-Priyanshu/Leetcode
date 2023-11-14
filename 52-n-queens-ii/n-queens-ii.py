class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(row, columns, diagonals, anti_diagonals, count):
            if row == n:
                return count + 1

            total_count = count
            for col in range(n):
                col_mask, diag_mask, anti_diag_mask = 1 << col, 1 << (row + col), 1 << (row - col + n - 1)

                if not (columns & col_mask) and not (diagonals & diag_mask) and not (anti_diagonals & anti_diag_mask):
                    total_count = solve(row + 1, columns | col_mask, diagonals | diag_mask, anti_diagonals | anti_diag_mask, total_count)

            return total_count

        return solve(0, 0, 0, 0, 0)