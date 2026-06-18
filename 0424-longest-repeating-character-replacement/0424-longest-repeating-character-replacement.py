class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hashh = {}
        window = 0
        ans = 0
        left = 0
        right = 0
        
        while right<n:
            
            window = right - left +1
            hashh[s[right]] = hashh.get(s[right],0)+1
            maxx = max(hashh.values())
            
            
            while window - maxx > k:
                maxx = max(hashh.values())
                window = right - left 
               
                hashh[s[left]]-=1
                left+=1
            ans = max(ans,window)
            right+=1
            
                
        return ans 
 
             
            


       
