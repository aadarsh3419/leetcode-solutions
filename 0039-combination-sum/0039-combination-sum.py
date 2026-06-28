class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        array = []
        def dfs(i,subset,remaining):
            if remaining == 0:
                array.append(subset.copy())
                return 
            if remaining < 0:
                return
            if i == len(candidates):
                
                return
           
            
            subset.append(candidates[i])
            remaining-=candidates[i]
            dfs(i,subset,remaining)
            
            remaining+=candidates[i]
            subset.pop() 
            dfs(i+1,subset,remaining)
        dfs(0,[],target)
        return array
