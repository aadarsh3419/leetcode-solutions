class Solution:
    def maxProduct(self, n: int) -> int:
        a = [ int(i) for i in str(n)]
        b = max(a)
        a.remove(b)
        c = max(a)
        return  b * c
