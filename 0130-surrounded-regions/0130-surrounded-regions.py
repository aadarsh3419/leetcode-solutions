class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        queue = deque()
        direction = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1)
        ]
        def bfs():
            while queue:
                r,c = queue.popleft()
                for dr,dc in direction:
                    nr = dr + r
                    nc = dc + c
                    if nr < 0 or nr >=n or nc < 0 or nc >= m:
                        continue
                    if board[nr][nc] == 'O':
                        queue.append((nr,nc))
                        board[nr][nc] = 'T'
        
        

        
        r = 0
        for c in range(m):
            if board[r][c] == 'O':
                board[r][c] = 'T'
                queue.append((r,c))
                
                
        r = n-1
        for c in range(m):
            if board[r][c] == 'O':
                board[r][c] = 'T'
                queue.append((r,c))
                
                
        c = 0
        for r in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'T'
                queue.append((r,c))
               
                
        c = m-1
        for r in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'T'
                queue.append((r,c))
                
        bfs()
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                
        
        
        return board
        
