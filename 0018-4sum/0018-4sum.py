class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        new_array = []
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                while k < l:
                    s = nums[i]+nums[j]+nums[k]+nums[l]
                    if s == target:
                        new_array.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k < l and nums[k] == nums[k-1]:
                            k+=1
                        while k < l and nums[l] == nums[l+1]: 
                            l-=1
                        continue
                    if s < target:
                        k+=1
                    else:
                        l-=1
        return new_array    

