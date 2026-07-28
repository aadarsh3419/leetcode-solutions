class Solution:
    def smallestPalindrome(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic.get(i,0)+1
        ans = ""
        for ch in sorted(dic):
            half = dic[ch]//2
            ans+=ch*half
            dic[ch]%=2
        mid = ""
        for ch in sorted(dic):
            if dic[ch] != 0:
                mid+=ch
        return ans + mid + ans[::-1]

       