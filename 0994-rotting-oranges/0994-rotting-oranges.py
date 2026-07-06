class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange = 0
        minutes = 0
        queue = deque()
        
        def bfs():
            nonlocal orange
            nonlocal minutes
            while queue:
                size = len(queue)
                change = False
                for _ in range(size): 
                    r,c = queue.popleft()
                    direction = [
                        (r-1,c),
                        (r+1,c),
                        (r,c-1),
                        (r,c+1)
                    ]
                    for dr,dc in direction:
                    
                        if dr >= len(grid) or dr < 0 or dc >= len(grid[0]) or dc< 0:
                            continue
                        if grid[dr][dc] == 1:
                            grid[dr][dc] = 2
                            change = True
                            queue.append((dr,dc))
                            orange-=1
                if change:
                    minutes+=1
                    
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    orange+=1
        bfs()
        
        if orange == 0:
            return minutes 
        if orange > 0:
            return -1
