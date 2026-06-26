class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = []
       
        def dfs(i,subset):
            
            if i == len(nums):
                array.append(subset.copy())
                return
            subset.append(nums[i])
            
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0,[])
        return array
