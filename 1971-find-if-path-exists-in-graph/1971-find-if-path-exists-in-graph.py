class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        

        def dfs(node):
            
            if node == destination:
                return True
            visited.add(node)
            for i in graph[node]:
                if  i not in visited:
                    if dfs(i):
                        return True
            return False
        return dfs(source)