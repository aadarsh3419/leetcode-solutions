class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = []
        x = 0
        for i in str(n):
            if i != '0':
                s.append(i)
                x = x + int(i)
        if not s:
            return 0
        st = "".join(s)
        return x*int(st)
        
                
        
        