class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        dicte = defaultdict(list)
        queue = deque()
        
        
        def bfs(start):
            while queue:
                node = queue.popleft()
                
                for i in graph[node]:
                    

                    if i in dicte and dicte[i] == dicte[node]:
                        return False
                    if i in dicte and dicte[i]!= dicte[node]:
                        
                        continue
                    if dicte[node] == "R":
                        dicte[i] = "B"
                        queue.append(i)
                    elif dicte[node] == "B":
                        dicte[i] = "R"
                        queue.append(i)
            return True
        result =True
        a = 0
        for i in range(len(graph)):
            if i not in dicte:
                dicte[i] = "R"
                queue.append(i)
                result = bfs(i)
                if result == False:
                    return False
            a+=1
        return True
        
       
                    
                    
            