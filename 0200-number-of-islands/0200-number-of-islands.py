class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c >=len(grid[0]):
                return
            if grid[r][c]== "0":
                return
            grid[r][c] = "0"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1": 
                    count+=1
                    dfs(i,j)
                
               
                
        return count