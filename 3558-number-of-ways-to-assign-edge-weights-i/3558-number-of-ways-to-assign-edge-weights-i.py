class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10**9+7
        graph = {}
        for u,v in edges:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node,parent):
            depth = 0
            for i in graph[node]:
                if i != parent:
                    depth = max(depth,1+dfs(i,node))
            return depth
        maxx =  dfs(1,-1)
        return (2**(maxx-1))%mod
        
