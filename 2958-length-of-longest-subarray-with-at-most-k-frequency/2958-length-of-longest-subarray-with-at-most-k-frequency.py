class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = {}
        n = len(nums)
        left = 0
        right = 0
        count = 0
        while right < n:
            hashmap[nums[right]] = hashmap.get(nums[right],0)+1
            if hashmap[nums[right]] <= k:
                count = max(count,right-left+1)
            while hashmap[nums[right]] > k:
                hashmap[nums[left]]-=1
                left+=1
            
            
                
                
            
            right+=1

            
        print(hashmap)
        return count