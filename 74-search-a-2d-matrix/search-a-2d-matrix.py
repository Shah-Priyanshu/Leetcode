import numpy as np

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        flat_matrix = np.array(matrix).flatten()
        index = np.searchsorted(flat_matrix, target)

        return index < len(flat_matrix) and flat_matrix[index] == target
