class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        # Initialize the result matrix with zeros
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                # Determine the value to assign to the current cell
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                
                # Subtract the assigned value from the row and column sums
                rowSum[i] -= value
                colSum[j] -= value
                
        return matrix
