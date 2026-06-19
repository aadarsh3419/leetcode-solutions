class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        i = 0
        j = n-1
        area = 0

        while i < j :
            width = j-i 
            if height[i] > height[j]:
                
                area = max(area,height[j] * width)
                j-=1
            else:
                area = max(area,height[i] * width)
                i+=1
        return area
            