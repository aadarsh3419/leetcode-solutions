class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxx = 0
       
        if n == 1:
            return 1
        for i in range(n):
            a = set()
            a.add(s[i])
            j = i+1
            while j < n:
                if s[j] in a:
                    maxx = max(maxx,j-i)
                    break
                else:
                    a.add(s[j])
                if j == n-1:
                    maxx = max(maxx,j-i+1)
                j+=1
        return maxx