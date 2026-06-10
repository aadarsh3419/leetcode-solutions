class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_sum = float('inf')
        n = len(nums)
        add = 0
        j= 0

        for i in range(n):
            add += nums[i]
            while add>=target:
                min_sum = min(min_sum,i-j+1)
                add-=nums[j]
                j+=1
        if min_sum!=float('inf'):
            return min_sum
        else:
            return 0