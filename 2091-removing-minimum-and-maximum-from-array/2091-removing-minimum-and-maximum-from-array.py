class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        left = 0
        mini = float("inf")
        mini_ind = 0
        maxi = float("-inf")
        maxi_ind = 0
        while left < len(nums):
            if nums[left] < mini:
                mini = nums[left]
                mini_ind = left
            if nums[left] > maxi:
                maxi = nums[left]
                maxi_ind = left
            left+=1
        i = min(mini_ind,maxi_ind)
        j = max(mini_ind,maxi_ind)
        n = len(nums)
        return min(j+1,n-i,i+1+n-j)
        print(mini_ind,maxi_ind)
        
        
