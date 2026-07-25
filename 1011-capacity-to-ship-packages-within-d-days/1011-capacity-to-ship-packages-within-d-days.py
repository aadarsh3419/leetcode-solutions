class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left+right)//2
            day = 1
            prefix = 0
            i = 0
            n  = len(weights)
            while i <= n-1:
                prefix+=weights[i]
                if prefix<=mid:
                    i+=1
                
                elif prefix > mid:
                    day+=1
                    prefix = 0 
            if prefix <= mid and i == n-1:
                day+=1
                    
                
            if day<=days:
                right = mid - 1
            elif day> days:
                left = mid+1
        return left


           