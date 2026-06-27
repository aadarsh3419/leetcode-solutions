class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        array = []
        def dfs(i,subset):
            if i == len(nums):
                array.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            a = subset.pop()
            next_i = i
            while next_i+1 <len(nums) and nums[next_i] == nums[next_i+1]:
                next_i+=1
            dfs(next_i+1,subset)
            
            
            
        dfs(0,[])
        
        return array