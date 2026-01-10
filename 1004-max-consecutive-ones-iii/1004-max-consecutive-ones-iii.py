class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=0
        ans=0
        i=0
        for j in range(len(nums)):
            if nums[j]==0: 
                count+=1
            while count>k:
                if nums[i] == 0:
                    count-=1
                i+=1
            ans = max(ans,(j-i+1))
        return ans
