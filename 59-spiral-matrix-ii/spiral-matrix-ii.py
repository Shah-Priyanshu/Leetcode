class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0]*n for i in range(n)]
        left,right=0,n-1
        top,bottom=0,n-1
        count=1
        while left<=right:
            for i in range(left,right+1):
                matrix[top][i]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=count
                count+=1
            right-=1
            for i in range(right,left-1,-1):
                matrix[bottom][i]=count
                count+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                matrix[i][left]=count
                count+=1
            left+=1
        return matrix

        