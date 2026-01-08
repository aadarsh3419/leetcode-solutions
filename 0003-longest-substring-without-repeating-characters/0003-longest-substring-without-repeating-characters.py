class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        i = 0
        last_seen = {}
        for j in range(len(s)):
            if s[j] in last_seen and last_seen[s[j]]>=i:
                i = last_seen[s[j]] + 1
            last_seen[s[j]] = j
            length = max(length,j-i+1)

        return length



