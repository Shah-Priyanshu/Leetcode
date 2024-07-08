class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  # This will store the position of the winner (0-based index)
        
        # Iterate from 1 to n to find the position of the winner
        for i in range(1, n + 1):
            winner = (winner + k) % i
        
        # Convert the 0-based index to a 1-based index
        return winner + 1