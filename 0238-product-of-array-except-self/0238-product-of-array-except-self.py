class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[1]*n
        right=1
        for i in range(n-1,-1,-1):
            ans[i]=right
            right*=nums[i]

        left=1
        for i in range(n):
            ans[i]*=left
            left*=nums[i]
        return ans


