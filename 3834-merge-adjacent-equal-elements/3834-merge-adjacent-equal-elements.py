class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            if stack and stack[-1] == i:
                temp = stack.pop()+i
                stack.append(temp)
            else:
                stack.append(i)
        return stack
            