import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        ans = []
        for i in nums:
            heapq.heappush(max_heap,-i)
        while max_heap:
            ans.append(-heapq.heappop(max_heap))
        return ans[k-1]
        