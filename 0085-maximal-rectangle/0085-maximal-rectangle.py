class Solution:
    def largestrectangle(self,heights):
        stack = []
        max_area = 0
        heights.append(0)
        for i ,h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                pop_heights = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area,pop_heights*width)
            stack.append(i)
        heights.pop()
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        colm,row = len(matrix[0]),len(matrix)
        height = [0]*colm
        max_area = 0
        for r in range(row):
            for c in range(colm):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
            max_area =  max(max_area,self.largestrectangle(height))
            
        return max_area
           


            
            