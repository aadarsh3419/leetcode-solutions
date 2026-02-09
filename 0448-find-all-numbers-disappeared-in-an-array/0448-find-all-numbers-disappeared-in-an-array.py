class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        n = set(nums)
        p = len(nums)
        for i in range(1,p+1):
            if i  not in n:
                output.append(i)
        return output
            