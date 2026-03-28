class Solution:
    def reverse(self, x: int) -> int:
        minus = "-"
        plus = "+"
        a = ""
        if x < 0:
            a+=minus
        s = str(abs(x))
        a+=s[::-1]
        p = int(a)
        if p > 2**31-1 or p < -2**31:
            return 0
        else:
            return p
            


        

            