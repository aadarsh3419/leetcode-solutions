class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        j = 0
        count = 0
        seen = set()
        
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[j])
                j+=1
           
            seen.add(s[i])
            count = max(count,i-j+1)
        return count
            
            
