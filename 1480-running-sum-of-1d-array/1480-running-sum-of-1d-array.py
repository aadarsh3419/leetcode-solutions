class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        e = []
        j = 0
        for i in nums:
            j=j+i
            e.append(j)
        return e
