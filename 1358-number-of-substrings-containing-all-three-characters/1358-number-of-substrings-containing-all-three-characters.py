class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        freq ={}
        n = len(s)
        
        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1
            while   'a' in freq and 'b' in  freq and 'c'in freq:
                count+=n-right
                freq[s[left]]-=1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left+=1
        return count
        