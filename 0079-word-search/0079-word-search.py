class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            found = (dfs(r-1,c,i+1) or
                    dfs(r+1,c,i+1) or
                    dfs(r,c-1,i+1) or
                    dfs(r,c+1,i+1))
            
            board[r][c] = temp
            
            return found
                
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
                
        
                
