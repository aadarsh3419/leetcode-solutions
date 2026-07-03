class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provision = 0
        def dfs(c):
            
            visited.add(c)
            
            
            for next_c in range(len(isConnected)):
                if isConnected[c][next_c] == 1:
                    if next_c not in visited:
                        visited.add(next_c)
                        dfs(next_c)
                    

        for i in range(len(isConnected)):
            if i not in visited:
                provision+=1
                dfs(i)
        return provision
        
   
        
            