class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = {}
        for u,v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node not in graph:
                return False
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    
                    if i == destination:
                        return True
            
                    if dfs(i):
                        return True
            return False
        
        if source == destination:
            return True
                    
        return dfs(source)
        
        

