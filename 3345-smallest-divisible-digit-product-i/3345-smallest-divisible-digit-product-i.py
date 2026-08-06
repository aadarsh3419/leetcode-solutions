class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digit = [int(i) for  i in str(n)]
            digit_pro = math.prod(digit)
            if digit_pro % t == 0:
                return n
                break
            else:
                n = n+1
        
        print(n)