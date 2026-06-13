class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            score = 0
            for ch in word:
                score+=weights[ord(ch)-ord('a')]
            result += chr(ord('z')-score%26)
        return result

       


  
 