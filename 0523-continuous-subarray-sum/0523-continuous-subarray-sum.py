class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashh = {0:-1}
        n = len(nums)
        prefix = 0
        
        for i in range(n):
            prefix += nums[i]
            diff = prefix % k
            if diff in hashh:
                if i-hashh[diff]>=2:
                    return True
            else:
                hashh[diff] = i
        return False
