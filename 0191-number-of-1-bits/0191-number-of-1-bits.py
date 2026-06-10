class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)[2:]
        b= len(a)
        count = 0
        for i in range(b):
            if a[i] == "1":
                count+=1
        return count
 