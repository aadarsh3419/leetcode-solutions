class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        answer = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                mid = stack.pop()
                height = heights[mid]
                right = i
                left = stack[-1] if stack else -1
                width = right - left - 1
                area = height*width
                answer = max(answer,area)
            stack.append(i)
        while stack:
            mid = stack.pop()
            height = heights[mid]
            right = n
            left = stack[-1] if stack else -1
            width = right - left -1
            area = height*width
            answer = max(answer,area)

            
        return answer
