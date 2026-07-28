class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        queue = deque()
        queue.append(0)
        ans = 0
        visited = set()
        visited.add(0)
        def bfs():
            nonlocal ans
            while queue:
                node = queue.popleft()
                for i,j in graph[node]:
                    
                    if i not in visited:
                        visited.add(i)
                        queue.append(i)
                        if j == 1:
                            ans+=1
                    
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))
        bfs()
        return ans