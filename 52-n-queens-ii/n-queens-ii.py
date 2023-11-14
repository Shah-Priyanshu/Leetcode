class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=[0]
        col=set()
        posDiag=set()
        negDiag=set()
        board=[['.' for i in range(n)] for j in range(n)]
        def backtrack(r):
            if r==n:
                count[0]+=1
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]='Q'
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]='.'
        backtrack(0)
        return count[0]