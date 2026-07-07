class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= n or c<0 or c>=m or  grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0 
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)  
                
        
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                   
                    count = max(count,dfs(i,j))
        return count