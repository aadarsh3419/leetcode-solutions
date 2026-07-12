class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def bfs(start,end):
            queue = deque([start])
            visited = {start}
            while queue:
                node = queue.popleft()
                if node == end:
                    return True
                for neibour in adj[node]:
                    if neibour not in visited:
                        visited.add(neibour)
                        queue.append(neibour)
            return False
        for u,v in edges:
            if bfs(u,v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)


            
            
            




        