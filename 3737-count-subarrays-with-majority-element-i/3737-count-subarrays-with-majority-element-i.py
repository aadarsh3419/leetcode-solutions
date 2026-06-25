class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            targetc = 0
            
            for j in range(i,n):
                if nums[j] == target:
                    targetc +=1
                lent = j - i + 1
                if 2*targetc > lent:
                    count+=1
                
        return count
