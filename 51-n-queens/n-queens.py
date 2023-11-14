class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def solve(row, columns, diagonals, anti_diagonals, current_solution):
            if row == n:
                solutions.append(current_solution[:])
                return

            for col in range(n):
                col_mask, diag_mask, anti_diag_mask = 1 << col, 1 << (row + col), 1 << (row - col + n - 1)

                if not (columns & col_mask) and not (diagonals & diag_mask) and not (anti_diagonals & anti_diag_mask):
                    columns ^= col_mask
                    diagonals ^= diag_mask
                    anti_diagonals ^= anti_diag_mask
                    current_solution.append(col)

                    solve(row + 1, columns, diagonals, anti_diagonals, current_solution)

                    columns ^= col_mask
                    diagonals ^= diag_mask
                    anti_diagonals ^= anti_diag_mask
                    current_solution.pop()

        solutions = []
        solve(0, 0, 0, 0, [])
        return [["." * col + "Q" + "." * (n - col - 1) for col in solution] for solution in solutions]
