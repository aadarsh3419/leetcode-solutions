class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        score = 0
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            score+=largest
            new_val = ceil(largest/3)
            heapq.heappush(max_heap,-new_val)
        return score



        
