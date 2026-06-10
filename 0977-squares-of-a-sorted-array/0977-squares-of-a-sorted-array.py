class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = [x**2 for x in nums]
        a.sort()
        return a