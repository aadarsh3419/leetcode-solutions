class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        a = float('inf')
        while left <= right:
            mid = (left+right)//2
            requ_h = 0
            for i in piles:
                requ_h += ceil(i/mid)  
            if requ_h <= h:
                right = mid - 1
                
            elif requ_h > h:
                left = mid+1
        return left
            
       
            