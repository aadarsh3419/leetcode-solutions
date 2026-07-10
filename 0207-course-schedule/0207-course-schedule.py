class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        incomining = [0]*numCourses
        for course,pre in prerequisites:
            adj[pre].append(course)
            incomining[course]+=1
        queue = deque()
        complete = 0
        def bfs():
            nonlocal incomining
            nonlocal complete
            while queue:
                ind = queue.popleft()
                a = adj[ind]
                for pre in a:
                    incomining[pre]-=1
                    if incomining[pre] == 0:
                        queue.append(pre)
                    
                complete+=1
                
                
        
        for i in range(len(incomining)):
            if incomining[i] == 0:
                queue.append(i)
        bfs()
        if complete==numCourses:
            return True
        else:
            return False 
       
        
         

