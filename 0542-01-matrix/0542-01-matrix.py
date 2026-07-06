class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        matr = [[-1]*len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    matr[i][j] = 0
                    queue.append((i,j))
        def bfs():
            while queue:
                 
                r,c = queue.popleft()
                direction = [
                        (r-1,c),
                        (r+1,c),
                        (r,c-1),
                        (r,c+1)
                    ]

                for dr,dc in direction:
                    if dr < 0 or dr >= len(mat) or dc < 0 or dc >= len(mat[0]):
                        continue
                    if mat[dr][dc] == 0:
                        continue
                    if mat[dr][dc] == 1:
                        if matr[dr][dc] == -1:
                            matr[dr][dc] = mat[dr][dc] + matr[r][c]   
                            queue.append((dr,dc))    
        bfs()
        return matr
