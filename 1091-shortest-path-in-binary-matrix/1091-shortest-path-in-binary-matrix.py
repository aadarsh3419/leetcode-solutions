class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        if n == 1 and  m == 1:
            return 1
        distance = 0
        queue.append((0,0))
        grid[0][0] = -1

        direction = [
                (-1,0),
                (1,0),
                (0,-1),
                (0,1),
                (1,1),
                (-1,-1),
                (-1,1),
                (1,-1)
        ]
        def bfs():
            nonlocal distance
            nonlocal m,n
            while queue:
                size = len(queue)
                for _ in range(size):
                    r,c = queue.popleft()
                    if r == n-1 and c == m-1:
                        return distance + 1
                    
                    for dr,dc in direction:
                        nr = dr + r
                        nc = dc + c
                        if nr < 0 or nr >= len(grid) or nc < 0 or nc >=len(grid [0]):
                            continue
                        if grid[nr][nc] == 1 or grid[nr][nc] == -1:
                            continue
                        if grid[nr][nc] == 0 :
                            queue.append((nr,nc))
                            grid[nr][nc] = -1
                    
                distance+=1
            return -1
                
        return bfs()