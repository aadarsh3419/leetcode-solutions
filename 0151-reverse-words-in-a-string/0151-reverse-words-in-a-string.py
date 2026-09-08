class Solution:
    def reverseWords(self, s: str) -> str:
        arry = s.split()
        return " ".join(arry[::-1])

