class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        

        for i in range(n):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:n])
            if left_sum == right_sum:
                return i
        return -1