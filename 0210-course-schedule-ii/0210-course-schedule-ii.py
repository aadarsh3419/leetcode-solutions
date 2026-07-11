class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        incoming = [0]*numCourses
        queue = deque()
        array = []
        complete = 0
        for course,pre in prerequisites:
            adj[pre].append(course)
            incoming[course]+=1
        def bfs():
            nonlocal complete
            while queue:
                ind = queue.popleft()
                
                a = adj[ind]
                for i in a:
                    
                    incoming[i] -=1
                    if incoming[i] == 0:
                        queue.append(i)
                        array.append(i)
                complete+=1
                
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
                array.append(i)
        bfs()
        if complete == numCourses:
            return array
        else:
            return []
        