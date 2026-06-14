class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        num = nums + nums
        n = len(num)
        stack = []
        for i in range(n):
            while stack and num[stack[-1]] < num[i]:
                
                idx = stack.pop()
                if idx < len(nums):
                    result[idx] = num[i] 
            stack.append(i)
        return result







