class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        string = {}
        
        for tex in text:
            string[tex] = string.get(tex,0)+1
        return min((string.get('b',0)//1),
                    (string.get('a',0)//1),
                    (string.get('l',0)//2),
                    (string.get('o',0)//2),
                    (string.get('n',0)//1)   )   
