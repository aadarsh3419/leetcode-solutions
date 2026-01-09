class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        
        max_freq = 0
        i = 0
        freq={}
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j],0)+1
             
            max_freq = max(max_freq,freq[s[j]])
            
            while (j-i+1) - max_freq > k:
                freq[s[i]]-=1
                i+=1
                
            ans = max(ans,j-i+1)
        return ans