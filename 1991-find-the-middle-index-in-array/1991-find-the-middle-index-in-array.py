class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n =len(nums)
        left_sum = 0
        right_sum = 0
        total_sum = sum(nums)
        for i in range(0,n):
            left_sum = sum(nums[0:i])
            right_sum = total_sum-left_sum-nums[i]
            if left_sum == right_sum:
                return i
        return -1