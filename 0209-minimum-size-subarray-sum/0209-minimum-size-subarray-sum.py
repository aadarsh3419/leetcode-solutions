class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum = 0
        e = float('inf')

        for j in range(len(nums)):
            sum+=nums[j]

            while sum >=target:

                e = min(e,j-i+1)
                sum -= nums[i]
                i+=1
        if e == float('inf'):
            return 0
        else:
            return e
        