class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicte,dicte1 = {},{}
        for i in range(len(s)):
            dicte[s[i]] = dicte.get(s[i],0)+1
            dicte1[t[i]] = dicte1.get(t[i],0)+1
        
        return dicte == dicte1