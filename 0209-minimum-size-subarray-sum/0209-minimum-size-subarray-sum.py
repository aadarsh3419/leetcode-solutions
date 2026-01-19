class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       n = len(nums)
       sum_window = 0
       store_len_min = float('inf')
       i = 0
       for j in range(0,n):
        sum_window+=nums[j]


        while sum_window >= target:
            store_len_min = min(store_len_min,j-i+1)
            sum_window-=nums[i]
            i+=1
       return 0 if store_len_min == float('inf') else store_len_min
