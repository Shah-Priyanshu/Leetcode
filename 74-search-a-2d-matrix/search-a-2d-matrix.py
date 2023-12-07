class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # using linear search (looping through the matrix) to take each list in it
        m = len(matrix)
        
        for i in range(m):
            lst = matrix[i]

            l = 0
            r = len(lst) - 1

            while l <= r:
                mid = (l + r) // 2
                if target > lst[mid]:
                    l = mid + 1
                elif target < lst[mid]:
                    r = mid - 1
                else:
                    return True
                    
        return False
