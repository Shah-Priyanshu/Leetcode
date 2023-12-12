from collections import Counter

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board),len(board[0])
        if len(word) > m*n:
            return False

        count = Counter(sum(board,[]))
        for c,countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        reqd = len(word)

        def legalcheck(x,y):
            return 0<=x<=m-1 and 0<=y<=n-1

        def process(node,i):
            x,y = node[0],node[1]
            
            if board[x][y] != word[i]:
                return False 

            if i == reqd:
                return True

            original = board[x][y]
            board[x][y] = '#'
            ans = True if i == reqd-1 else False
            
            for delta in [-1,1]:
                if legalcheck(x+delta,y):
                    ans = ans or process((x+delta,y),i+1)
                if legalcheck(x,y+delta):
                    ans = ans or process((x,y+delta),i+1)

            board[x][y] = original
            return ans

        for i in range(m):
            for j in range(n):
                result = process((i,j),0)
                if result:
                    return result

        return False