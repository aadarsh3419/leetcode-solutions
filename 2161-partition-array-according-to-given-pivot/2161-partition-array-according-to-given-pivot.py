class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        stack = []
        stack1 = []
        stack3 = []
        for i in nums:
            if i < pivot:
                stack.append(i)
            if i > pivot:
                stack1.append(i)
            if i == pivot:
                stack3.append(i)
                
        stack4 = stack+stack3+stack1
        return stack4
