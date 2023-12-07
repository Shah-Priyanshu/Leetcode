class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top = 0               
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break
        row = mid
        lo = 0
        hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if target < matrix[row][mid]:
                hi = mid - 1
            elif target > matrix[row][mid]:
                lo = mid + 1
            else:
                return True
        
        return False