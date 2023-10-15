class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets to keep track of digits in rows, columns, and 3x3 sub-boxes.
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        subbox_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell_value = board[i][j]
                if cell_value != ".":
                    # Check the current row for duplicates.
                    if cell_value in row_sets[i]:
                        return False
                    row_sets[i].add(cell_value)

                    # Check the current column for duplicates.
                    if cell_value in col_sets[j]:
                        return False
                    col_sets[j].add(cell_value)

                    # Check the current 3x3 sub-box for duplicates.
                    subbox_index = (i // 3) * 3 + j // 3
                    if cell_value in subbox_sets[subbox_index]:
                        return False
                    subbox_sets[subbox_index].add(cell_value)

        return True
