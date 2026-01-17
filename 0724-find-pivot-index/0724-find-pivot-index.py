class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        all_total = 0
        for i in range(n):
            all_total += nums[i]
        for i in range(n):
            
            right_sum = all_total-left_sum - nums[i]
           

            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1