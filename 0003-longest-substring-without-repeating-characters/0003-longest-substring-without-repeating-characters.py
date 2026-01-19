class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        i = 0
        n = len(s)
        last_seen = {}
        for j in range(n):
            if s[j] in last_seen:
                i = max(i,last_seen[s[j]]+1)
            last_seen[s[j]] = j
            length = max(length,j-i+1)
        return length
            


