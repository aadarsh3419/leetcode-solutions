class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left<=right:
            mid = (left+right)//2
            day = 1
            prefix = 0
            for i in weights:
                if prefix + i <= mid:
                    prefix+=i
                else:
                    day+=1
                    prefix = i

            if day<=days:
                right = mid - 1
            elif day> days:
                left = mid+1
        return left


           