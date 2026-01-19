class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        n = len(nums)
        for i in range(n):
            current_sum+=nums[i]
            max_sum = max(max_sum,current_sum)
            if current_sum<0:
                current_sum =0
        return max_sum