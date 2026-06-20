class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        array = []
        for i in range(n):
            for j in range(n-1,i,-1):
                c = i+1
                d = j-1
                if i>0 and nums[i] == nums[i-1]:
                    continue
                if j < n-1 and nums[j] == nums[j+1]:
                    continue
                while c < d:
                    e = nums[i] + nums[c] + nums[d] + nums[j]
                    
                    
                    if e == target:
                        array.append([nums[i],nums[c],nums[d],nums[j]])
                        c+=1
                        d-=1
                        while c < d and nums[c] == nums[c-1] :
                            c+=1
                        while d > c and nums[d] == nums[d+1]:
                            d-=1
                    elif e > target:
                        d-=1 
                    else:
                        c+=1
                    
        return array

