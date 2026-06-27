class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        array = []
        def dfs(i):
            if i == len(nums):
                array.append(nums.copy())
                return
            for j in range(i, len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                


                dfs(i+1)  
                nums[i],nums[j] = nums[j],nums[i]
  
        dfs(0) 
        return array

            