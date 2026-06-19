class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        print(n)
        
        m = len(haystack)
        windwo = 0
        left = 0
        right = 0
        while right < m:
            window = right - left + 1
            if window == n:
                result = haystack[left:right+1]
                print(result)
                if result == needle:
                    return left 
                left+=1
                window-=1
            right+=1
        return -1

                
        
        