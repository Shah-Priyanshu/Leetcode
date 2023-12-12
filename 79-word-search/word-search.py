class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(i, j, k):
            # Check if the current cell is out of bounds or the letter doesn't match
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            
            # Check if the word is found
            if k == len(word) - 1:
                return True
            
            # Mark the current cell as visited
            temp, board[i][j] = board[i][j], '/'
            
            # Explore all possible directions (up, down, left, right)
            result = (backtrack(i + 1, j, k + 1) or
                      backtrack(i - 1, j, k + 1) or
                      backtrack(i, j + 1, k + 1) or
                      backtrack(i, j - 1, k + 1))
            
            # Restore the original value of the cell
            board[i][j] = temp
            
            return result

        # Iterate through each cell in the grid to start the search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        
        # If the loop completes without finding the word, return False
        return False