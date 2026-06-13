class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        graph = {}
        for i,w in enumerate(weights):
            graph[chr(ord("a")+i)] = w
        result = ""
        for word in words:
            score = 0
            for ch in word:
                score+=graph[ch]
            idx = score%26
            result += chr(ord("z")-idx)
        return result
       


  
