class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n ==1:
            return True
        max_e = 0
        for i in range(n):
            if i>max_e:
                return False
            max_e = max(max_e,i + nums[i])
            if max_e >= n-1:
                return True
        return True