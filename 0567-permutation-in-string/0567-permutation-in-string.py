class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_m = {}
        n = len(s1)
        for i in range(n):
            hash_m[s1[i]] = hash_m.get(s1[i],0)+1
        m = len(s2)
        left = 0
        right = 0
        window = 0
        hashh = {}
        while right < m:
            
            hashh[s2[right]] = hashh.get(s2[right],0)+1
            window = right - left + 1
            if window == n:
                if hashh == hash_m:
                    return True
                hashh[s2[left]]-=1
                if hashh[s2[left]] == 0:
                    del hashh[s2[left]]
                window-=1
                left+=1
            
            
            right+=1
            
        if window == n:
            if hashh == hash_m:
                return True
            
        
        return False

        
            
