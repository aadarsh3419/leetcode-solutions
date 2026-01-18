class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        i = 0
        j = h-1
        right_max = 0
        left_max = 0
        trap = 0
        while i < j:
            left_max = max(left_max,height[i])
            right_max = max(right_max,height[j])
            if left_max <= right_max:
                trap+=left_max-height[i]
                i+=1
            else:
                trap+=right_max - height[j]
                j-=1
        return trap