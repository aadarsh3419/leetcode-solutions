class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        queue = deque()
        for i in range(n):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            while queue and queue[0] < i-k+1:
                queue.popleft()
            queue.append(i)
            if i >= k-1:
                result.append(nums[queue[0]])
            
        return result 
            
