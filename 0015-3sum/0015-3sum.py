class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        p = []
        nums.sort()
        for i ,v in enumerate(nums):
            if i>0:
                if nums[i] == nums[i-1]:
                    continue
            j = i+1
            k =len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s == target:
                    p.append([nums[i],nums[j],nums[k]])
                    while j <k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif s < 0:
                    j+=1
                else:
                    k-=1
        return p
                

