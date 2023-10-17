class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(num, row, col):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, row, col):
                                board[row][col] = num
                                if backtrack():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        backtrack()
