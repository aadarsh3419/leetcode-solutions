class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        array = []
        array.append([])
        def dfs(i,subset):
            
            if i == len(nums):
                return
            subset.append(nums[i])
            array.append(subset.copy())
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0,[])
        return array
