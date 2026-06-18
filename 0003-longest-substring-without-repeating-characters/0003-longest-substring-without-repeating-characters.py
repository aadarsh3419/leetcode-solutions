class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxx = 0
        a = set()
        if n == 1:
            return 1

        left = 0
        right = 0
        
        while right < n:
            while s[right] in a:
                maxx = max(maxx,right-left)
                a.remove(s[left])
                left+=1 
            else:
                a.add(s[right])
                
                maxx= max(maxx,right-left+1)
                right+=1
        return maxx
            

            
            