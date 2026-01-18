class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        if h ==0:
            return 0
        left_max = [0]*h
        right_max = [0]*h
        left_max[0]=height[0]
        for i in range(1,h):
            left_max[i] = max(left_max[i-1],height[i])
        right_max[h-1] = height[h-1]
        for i in range(h-2,-1,-1):
            right_max[i]=max(right_max[i+1],height[i])
        trap=0
        for i in range(h):
            trap+=max(0,min(left_max[i],right_max[i])) - height[i]
        return trap


            
        return trap