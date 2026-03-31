from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()
        

        

    def ping(self, t: int) -> int:
        p = t-3000
        self.queue.append(t)
        while self.queue and self.queue[0] < p:
            self.queue.popleft()
        
        s = len(self.queue)
        return s

            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)