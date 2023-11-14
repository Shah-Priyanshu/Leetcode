class Solution(object):
    def solveNQueens(self, n):
        board=[["."]*n for i in range(n)]
        pos=set()
        neg=set()
        col=set()
        res=[]
        def backtrack(r):
            if(r==n):
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for i in range(0,n):
                if(i in col or (r+i) in pos or (r-i) in neg):
                    continue
                
                board[r][i]="Q"
                pos.add(r+i)
                neg.add(r-i)
                col.add(i)

                backtrack(r+1)

                board[r][i]="."
                pos.remove(r+i)
                neg.remove(r-i)
                col.remove(i)
        backtrack(0)
        return res