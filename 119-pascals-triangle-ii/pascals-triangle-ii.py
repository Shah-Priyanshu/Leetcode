class Solution(object):
    def getRow(self, rowIndex):
        res=[1]
        for i in range(1,rowIndex+1):
            res.append(1)
            for j in range(len(res)-2,0,-1):
                res[j]+=res[j-1]
        return res        