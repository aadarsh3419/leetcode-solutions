class Solution:
    def hIndex(self, citations: List[int]) -> int:
         citations.sort(reverse = True)
         n = len(citations)
         h = 0
         i = 0 
         while True:
            if i==n:
                break
            elif citations[i]>=i+1:
                h = h+1
            i+=1
         return h
