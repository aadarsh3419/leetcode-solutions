class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for i in nums2:
            while stack and stack[-1] < i:
                next_greater[stack.pop()] = i
            stack.append(i)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num]for num in nums1]


        
                


                    