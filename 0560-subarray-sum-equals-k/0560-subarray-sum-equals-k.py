class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
        ans = 0
        
        for num in nums:
            prefix += num
            old = prefix - k
            
            if old in count:
                ans += count.get(old,0)
            count[prefix] = count.get(prefix,0)+1
        return ans

        