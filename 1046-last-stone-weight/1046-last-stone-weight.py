import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            first = -heapq.heappop(heap)
            secound = -heapq.heappop(heap)
            if(first!=secound):
                a = first-secound
                heapq.heappush(heap,-a)
            
        if heap:
            return -heap[0]
        return 0