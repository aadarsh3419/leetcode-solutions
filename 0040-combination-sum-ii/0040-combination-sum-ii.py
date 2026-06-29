class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        array = []
        def dfs(i,subset,remaining):
            if remaining == 0:
                array.append(subset.copy())
                return
            
            if i  == len(candidates) or remaining < 0:
                return
            #we first append the i in subset then minus it with target then recall it until 1 condtion hit abouve then we pop the last element and add the minus we do before undo the remaning then

            subset.append(candidates[i])
            dfs(i+1,subset,remaining-candidates[i])
            subset.pop()
            
            #with this loop we skip the same element which is already used then increase the i call the recursion 
            next_i = i
            while next_i+1 < len(candidates) and candidates[next_i] == candidates[next_i+1]:
                next_i+=1
                
            dfs(next_i+1,subset,remaining)
        dfs(0,[],target)
        return array
