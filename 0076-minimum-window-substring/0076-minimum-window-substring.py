class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        hash1 = {}
        for i in range(n):
            hash1[t[i]] = hash1.get(t[i],0)+1
        m = len(s)
        hash2 = {}
        bl = float("inf")
        left = 0
        right = 0
        window = 0
        best = 0
        
        while right < m:
            valid = True
            hash2[s[right]] = hash2.get(s[right],0)+1
            for ch in hash1:
                if hash2.get(ch,0)<hash1[ch]:
                    valid = False
                    break
            
            while valid:

                window = right - left + 1
                if window < bl:
                    bl = window
                    best = left
                hash2[s[left]] -=1 
                if hash2[s[left]] == 0: 
                    del hash2[s[left]]
                left+=1
                for ch in hash1:
                    if hash2.get(ch,0) < hash1[ch]:
                        valid = False
            right+=1
        if bl == float("inf"):
            return ""
        else:
            return s[best:best+bl]
                




        




        