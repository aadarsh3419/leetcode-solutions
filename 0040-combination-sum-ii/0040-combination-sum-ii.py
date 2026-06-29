class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        array = []
        def dfs(i,subset,remaining):
            if remaining == 0:
                array.append(subset.copy())
                return
            if remaining < 0:
                return
            if i  == len(candidates):
                return
            subset.append(candidates[i])
            remaining-=candidates[i]
            dfs(i+1,subset,remaining)
            subset.pop()
            remaining+=candidates[i]
            next_i = i
            while next_i+1 < len(candidates) and candidates[next_i] == candidates[next_i+1]:
                next_i+=1
            dfs(next_i+1,subset,remaining)
        dfs(0,[],target)
        return array
