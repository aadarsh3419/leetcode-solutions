class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        n = []
        for i in digits:
            a += str(i)
        p = int(a)+1
        a = str(p)
        for i in a:
            n.append(int(i))
        return n
            
        