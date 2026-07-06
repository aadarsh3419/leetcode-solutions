class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        matr = [[-1]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    matr[i][j] = 0
                    queue.append((i,j))
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
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= len(mat) or nc < 0 or nc >= len(mat[0]):
                        continue
                    
                    if mat[nr][nc] == 1 and matr[nr][nc] == -1:
                        
                            matr[nr][nc] = matr[r][c] +1
                            queue.append((nr,nc))    
        bfs()
        return matr
