class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
       
        i = 1
        while True:
            a = k*i
            if a not in nums:
                return a 
            i+=1
            
