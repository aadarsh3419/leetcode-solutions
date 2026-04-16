class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def can_finish(time):
            total = 0
            
            for w in workerTimes:
                # Solve k(k+1)/2 * w <= time
                # => k(k+1) <= 2*time / w
                x = (2 * time) // w
                
                k = int((math.sqrt(1 + 4 * x) - 1) // 2)
                
                total += k
                if total >= mountainHeight:
                    return True
            
            return False
        
        left, right = 0, 10**18
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans