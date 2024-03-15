class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        
        def bfs(x, y):
            if board[x][y] != 'O':
                return
            # Queue for BFS
            queue = collections.deque([(x, y)])
            while queue:
                x, y = queue.popleft()
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    board[x][y] = 'E'  # Mark as edge-connected and not flippable
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 4-directional
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                            queue.append((nx, ny))
        
        # Mark unflippable 'O's using BFS from border 'O's
        for i in range(m):
            bfs(i, 0)
            bfs(i, n-1)
        for j in range(n):
            bfs(0, j)
            bfs(m-1, j)
                
        # Flip surrounded 'O's to 'X's and revert 'E's back to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'

# Import collections for deque
import collections
