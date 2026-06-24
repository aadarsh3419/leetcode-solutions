class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmostk(nums,k) - self.atmostk(nums,k-1)
    def atmostk(self,nums,k): 
        hashh = {}
        n = len(nums)
        left = 0
        count = 0
        odd = 0
        for right in range(n):
            
            hashh[nums[right]] = hashh.get(nums[right],0)+1
            if nums[right]%2!=0:
                odd+=1
            
            while odd > k:
                hashh[nums[left]]-=1
                if nums[left]%2!=0:
                    odd-=1
                left+=1
            count += right-left+1
        return count