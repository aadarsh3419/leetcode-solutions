class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        arry = []
        for i in range(n):
            if nums[i]!=val:
                arry.append(nums[i])  
        for i in range(len(arry)):
            nums[i] = arry[i]
        return len(arry)