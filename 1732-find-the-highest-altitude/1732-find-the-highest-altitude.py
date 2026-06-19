class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        a = 0
        maxx = 0
        for g in gain:
            a+=g
            
            maxx = max(maxx,a)
        return maxx
        
