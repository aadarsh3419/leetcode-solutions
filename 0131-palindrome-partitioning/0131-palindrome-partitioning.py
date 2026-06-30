class Solution:
    def partition(self, s: str) -> List[List[str]]:
        array = []
        def dfs(i,substring):
            if i == len(s):
                array.append(substring.copy())
                return
            for j in range(i,len(s)): 
                curr = s[i:j+1]
                print(curr)
                if curr == curr[::-1]: 
                    substring.append(curr)
                    dfs(j+1,substring)
                    substring.pop()

                
                    
                 
        dfs(0,[])
        return array
