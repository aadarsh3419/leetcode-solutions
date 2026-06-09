class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a = max(nums)
        b = min(nums)
        c = (a-b)*k
        return c