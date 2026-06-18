class Solution:
    def fib(self, n: int) -> int:
        
        def fiv(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            ans = fiv(n-1) + fiv(n-2) 
            return ans  
        return fiv(n)     