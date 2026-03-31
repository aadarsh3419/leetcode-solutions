import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        ans = 0
        for i in nums:
            heapq.heappush(max_heap,i)
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        return max_heap[0]
                

        