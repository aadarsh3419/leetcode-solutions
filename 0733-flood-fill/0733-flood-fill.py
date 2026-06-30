class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        orignal = image[sr][sc]
        def dfs(r,c):
            if r < 0 or r >= len(image) or c >= len(image[0]) or c < 0:
                return
            
            if image[r][c] != orignal:
                
                return
            image[r][c] = color
            
            dfs(r-1,c)
            
                
            dfs(r,c-1) 
                
            dfs(r+1,c)
                
            dfs(r,c+1)
            
                
            
        dfs(sr,sc)
        return image
        
