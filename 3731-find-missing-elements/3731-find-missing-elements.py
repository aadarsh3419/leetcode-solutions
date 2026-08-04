class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = min(nums)
        b = max(nums)
        arry = []
        for i in range(a,b):
            if i not in nums:
                arry.append(i)
        return arry