class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = len(s)
        ans = ""
        
        for i in range(p):
            left = i
            right = i
            while left >=0 and right < p and s[left] == s[right]:
                if(right-left+1)>len(ans):
                    ans = s[left:right+1]
                left-=1
                right+=1

            left = i
            right = i+1
            while left>=0 and right < p and s[left] == s[right]:
                if(right-left+1)>len(ans):
                    ans = s[left:right+1]
                left-=1
                right+=1
        
        return ans
            
            

        